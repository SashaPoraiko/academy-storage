from ..views import StorageAuthModelPaginateMixin
from ..models import Storage
from .serializers import StorageReadSerializer, StorageWriteSerializer, StorageFilterSerializer


class StorageViewSet(StorageAuthModelPaginateMixin):
    queryset = Storage.objects.all()
    serializer_class = StorageReadSerializer
    filter_serializer = StorageFilterSerializer

    def create(self, request, *args, **kwargs):
        self.serializer_class = StorageWriteSerializer
        return super().create(request, args, kwargs)

    def update(self, request, *args, **kwargs):
        self.serializer_class = StorageWriteSerializer
        return super().update(request, args, kwargs)
