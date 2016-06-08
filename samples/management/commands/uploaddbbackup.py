from django.core.management.base import BaseCommand, CommandError
from django.conf import settings

from boto.s3.connection import S3Connection
from os.path import exists, isfile, basename

if hasattr(settings, 'DB_BACKUP_PREFIX'):
    DB_BACKUP_PREFIX = settings.DB_BACKUP_PREFIX
else:
    DB_BACKUP_PREFIX = 'backups/db/'

AWS_ACCESS_KEY_ID = settings.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY = settings.AWS_SECRET_ACCESS_KEY
AWS_S3_HOST = settings.AWS_S3_HOST
AWS_STORAGE_BUCKET_NAME = settings.AWS_STORAGE_BUCKET_NAME

class HCP:
    def __init__(self, aws_id, aws_secret, server, bucket, prefix=''):
        hs3 = S3Connection(aws_access_key_id=aws_id,
                           aws_secret_access_key=aws_secret,
                           host=server)
        self.bucket = hs3.get_bucket(bucket)
        self.prefix = prefix

    def exists(self, name):
        return self.bucket.get_key(name) is not None

    def put(self, name, data):
        self.bucket.new_key(name).set_contents_from_string(data)

    def get(self, name):
        return self.bucket.get_key(name, validate=False).get_contents_as_string()

    def upload(self, local_name):
        if isfile(local_name):
            name = "%s%s" % (self.prefix, basename(local_name))
            if not self.exists(name):
                self.bucket.new_key(name).set_contents_from_filename(local_name)

    def download(self, key_name):
        """Fetch file if there is no local copy or hash is different to HCP
           to current directory
        """
        #Flat structure for now
        fn = basename(key_name)

        key = self.bucket.get_key(key_name)
        md5 = key.etag[1 :-1]

        local_md5 = hashfile(fn, hashlib.md5())

        if not local_md5 == md5:
            key.get_contents_to_filename(fn)

    def items(self, prefix=None):
        if prefix is None:
            prefix = self.prefix
        return self.bucket.list(prefix=prefix)


class Command(BaseCommand):
    help = 'Upload file to the bucket of this application'

    def add_arguments(self, parser):
        parser.add_argument('file_name')
        parser.add_argument('--prefix',
            default=DB_BACKUP_PREFIX,
            help='Upload a local file with this prefix to make it looks like in a file system with directory in object store')

    def handle(self, *args, **options):
        fn = options['file_name']
        if not isfile(fn):
            raise CommandError('File "%s" does not exist' % fn)

        self.stdout.write('About to upload file "%s" to the object store with prefix = %s' % (fn, options['prefix']))
        try:
            hs3 = HCP(AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY, AWS_S3_HOST, AWS_STORAGE_BUCKET_NAME, options['prefix'])
            hs3.upload(fn)
        except Exception as e:
            self.stderr.write('Failed to upload file "%s" to the object store with prefix = %s' % (fn, options['prefix']))
            self.stderr.write(str(e))

