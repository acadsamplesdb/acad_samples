import os
import glob
import re
SAMPLE_ID = re.compile(r"^ACAD([0-9]+).+$")

from django.core.management.base import BaseCommand, CommandError
from django.shortcuts import get_object_or_404
from django.core.files import File

from boto.exception import S3ResponseError, S3CreateError, BotoClientError

from samples.models import FileAttachment, Sample, Project, Permit, Extraction, Amplification, Enrichment


class Command(BaseCommand):
    help = 'Upload attachments (ACAD + object_id + string + .jpg) to an object from a folder. The default object is Sample.'

    def add_arguments(self, parser):
        parser.add_argument('dir_name')

        parser.add_argument('--model',
            default='Sample',
            choices=['Sample', 'Project', 'Permit', 'Extraction', 'Amplification', 'Enrichment'],
            help='Attach files to specifid model')

    def handle(self, *args, **options):
        if not os.path.exists(options['dir_name']):
            raise CommandError('Folder "%s" does not exist' % options['dir_name'])

        self.stdout.write('About to attach files in "%s" to the named %s' % (options['dir_name'], options['model']))

        files = glob.glob(options['dir_name'] + "/ACAD*.*")
        print(files)
        for fn in files:
            if os.path.isfile(fn):
                bn = os.path.basename(fn)
                gs = SAMPLE_ID.match(bn)
                if gs:
                    self.attach_file(fn, gs.group(1))
                else:
                    self.stdout.write('%s cannot be parsed' % bn)

    def attach_file(self, fn, pk, model=Sample):
        try:
            target = model.objects.get(pk=pk)
            print(target)

            f = open(fn, 'rb')
            attachment = FileAttachment(file=File(f))
            try:
                attachment.save()
                target.file.add(attachment)
                target.save()
                self.stdout.write('%s has been attached to sample.pk = %s' % (fn, pk))
            except (S3ResponseError, S3CreateError, BotoClientError) as e:
                self.stderr.write('Storage error raised when attaching file "%s" to sample.pk = %s. Exception detail: ' % (fn, pk))
                self.stderr.write(str(e))
            except Exception as e:
                self.stderr.write('Failed to attach file "%s" to sample.pk = %s. Exception detail: ' % (fn, pk))
                self.stderr.write(str(e))
            else:
                f.close()
        except model.DoesNotExist:
            self.stderr.write('Model canot be found with pk = "%s"' % pk)
        except Exception as e:
            self.stderr.write(str(e))
