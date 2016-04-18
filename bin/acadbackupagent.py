#!/usr/bin/env python3

"""
Backup objects in object store to file system.
"""

import base64
import hashlib
from boto.s3.connection import S3Connection
from os.path import exists, isfile
import sys
import json
import concurrent.futures

# HCP #facepalm
import ssl
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

def hashfile(file_name, hasher, blocksize=65536):
    """Return hash or NO FILE FOUND which is not a hash string"""
    if exists(file_name):
        with open(file_name, 'rb') as f:
            buf = f.read(blocksize)
            while len(buf) > 0:
                hasher.update(buf)
                buf = f.read(blocksize)
        return hasher.hexdigest()
    else:
        return "NO FILE FOUND"

class HCP:
    def __init__(self, aws_id, aws_secret, server, bucket):
        aws_id = base64.b64encode(bytes(aws_id, "utf-8")).decode()
        aws_secret = hashlib.md5(bytes(aws_secret, "utf-8")).hexdigest()
        hs3 = S3Connection(aws_access_key_id=aws_id,
                           aws_secret_access_key=aws_secret,
                           host=server)
        self.bucket = hs3.get_bucket(bucket)

    def exists(self, name):
        return name in self.bucket

    def put(self, name, data):
        self.bucket.new_key(name).set_contents_from_string(data)

    def get(self, name):
        return self.bucket.get_key(name, validate=False).get_contents_as_string()

    def check_local(self, fn):
        if not exists(fn):
            return

    def fetch(self, name):
        """Fetch file if there is no local copy or hash is different to HCP"""
        fn = name.split("/")[-1]

        key = self.bucket.get_key(name)
        md5 = key.etag[1 :-1]

        local_md5 = hashfile(fn, hashlib.md5())

        if local_md5 == md5:
            print("No action for %s" % fn)
        else:
            print("Need to download %s" % fn)
            key.get_contents_to_filename(fn)

    def items(self, prefix=None):
        return self.bucket.list(prefix=prefix)

if __name__ == '__main__':
    # The script requires a single positonal argument: path to the JSON config file with these keys:
    # {
    #   "host": "acad",
    #   "base": "file",
    #   "access": "samples",
    #   "secret": "pass",
    #   "bucket": "samples-data"
    # }
    if len(sys.argv) != 2:
        print("Please provide the path of configuration file with all the connection information")
        exit(1)
    conf_file = sys.argv[1]

    if not isfile(conf_file):
        print("Config file %s cannot be found" % conf_file)
        exit(1)

    with open(conf_file, 'r') as f:
        config = json.load(f)

    hcp = HCP(config['access'], config['secret'], config['host'], config['bucket'])
    items = hcp.items(config['base'])
    prefix = 'files'
    all_items = [item.name for item in hcp.items(prefix=prefix) if not item.name.endswith("/")]

    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        for item in all_items:
            executor.submit(hcp.fetch, item)
