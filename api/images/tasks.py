from __future__ import absolute_import, unicode_literals
import datetime
import os
import re
from django.conf import settings
from django.utils import timezone
from api.images.models import Image
from celery import shared_task
from celery.utils.log import get_task_logger


logger = get_task_logger(__name__)


@shared_task()
def loadimages():
    image_dir = settings.SINGULARITY_IMAGE_DIR
    p = re.compile('_(.*)--')
    files = [f for f in os.listdir(image_dir) if os.path.isfile(os.path.join(image_dir, f))]
    for f in files:
        statinfo = os.stat(os.path.join(image_dir, f))
        try:
            image_rec = Image.objects.get(name=f)
            logger.info('Found singularity image, {}.'.format(image_rec.name))
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
