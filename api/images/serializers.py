from rest_framework import serializers
from .models import Image


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ('url', 'id', 'name', 'size_in_bytes', 'version', 'created', 'updated')
        extra_kwargs = {
            'url': {
                'view_name': 'image-detail',
            }
        }
