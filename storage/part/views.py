from rest_framework import viewsets

from ..models import Part
from ..views import StorageAuthMixin

from .serializers import PartReadSerializer, PartFilterSerializer, PartWriteSerializer


class PartViewSet(StorageAuthMixin, viewsets.ModelViewSet):
    queryset = Part.objects.all()
    serializer_class = PartReadSerializer
    filter_serializer = PartFilterSerializer

    def create(self, request, *args, **kwargs):
        self.serializer_class = PartWriteSerializer
        return super().create(request, args, kwargs)

    def update(self, request, *args, **kwargs):
        self.serializer_class = PartWriteSerializer
        return super().update(request, args, kwargs)
