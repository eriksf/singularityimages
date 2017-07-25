import datetime
import os
import re
from django.conf import settings
from django.core.management.base import BaseCommand
from django.utils import timezone
from api.images.models import Image


class Command(BaseCommand):
    help = 'Load singularity images into the db.'

    def handle(self, *args, **options):
        image_dir = settings.SINGULARITY_IMAGE_DIR
        p = re.compile('_(.*)--')
        files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
        for f in files:
            statinfo = os.stat(os.path.join(image_dir, f))
            try:
                image_rec = Image.objects.get(name=f)
                print('Found image {}'.format(image_rec))
            except Image.DoesNotExist:
                try:
                    version = p.search(f).group(1)
                except AttributeError:
                    version = ''
                created = timezone.make_aware(datetime.datetime.fromtimestamp(statinfo.st_ctime),
                                              timezone.get_current_timezone())
                updated = timezone.make_aware(datetime.datetime.fromtimestamp(statinfo.st_mtime),
                                              timezone.get_current_timezone())
                image = Image(name=f,
                              size_in_bytes=statinfo.st_size,
                              version=version,
                              created=created,
                              updated=updated)
                image.save()
