from os.path import join, getsize
from django.conf import settings
from rest_framework import renderers


class Bzip2ArchiveRenderer(renderers.BaseRenderer):
    media_type = 'application/x-bzip2'
    format = 'bz2'
    charset = None
    render_style = 'binary'
    image_dir = settings.SINGULARITY_IMAGE_DIR

    def set_filename(self, name, renderer_context):
        type_name = 'attachment; filename={}'.format(name)
        try:
            renderer_context['response']['Content-Disposition'] = type_name
        except Exception:
            pass

    def set_response_length(self, length, renderer_context):
        try:
            renderer_context['response']['Content-Length'] = length
        except Exception:
            pass

    def render(self, data, media_type=None, renderer_context=None):
        image_path = join(self.image_dir, data)
        image_filesize = getsize(image_path)
        with open(image_path, 'rb') as f:
            contents = f.read()
        self.set_filename(data, renderer_context)
        self.set_response_length(image_filesize, renderer_context)
        return contents

