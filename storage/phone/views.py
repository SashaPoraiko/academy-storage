from ..models import Phone
from ..views import StorageAuthModelPaginateMixin

from .serializers import PhoneWriteSerializer, PhoneReadSerializer, PhoneFilterSerializer


class PhoneViewSet(StorageAuthModelPaginateMixin):
    queryset = Phone.objects.all()
    serializer_class = PhoneReadSerializer
    filter_serializer = PhoneFilterSerializer
    filter_parse_query_params = (('date-create-from', 'date_create_from'),)

    def create(self, request, *args, **kwargs):
        self.serializer_class = PhoneWriteSerializer
        return super().create(request, args, kwargs)

    def update(self, request, *args, **kwargs):
        self.serializer_class = PhoneWriteSerializer
        return super().update(request, args, kwargs)
