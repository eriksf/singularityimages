from rest_framework import viewsets
from rest_framework.decorators import detail_route
from rest_framework.response import Response
from .models import Image
from .serializers import ImageSerializer
from .renderers import BinaryRenderer


# Create your views here.
class ImageViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

    @detail_route(renderer_classes=[BinaryRenderer])
    def download(self, request, *args, **kwargs):
        image = self.get_object()
        return Response(image.name)
