from rest_framework import viewsets

from ..models import Phone
from ..views import StorageAuthModelPaginateMixin, StorageAuthMixin

from .serializers import PhoneWriteSerializer, PhoneReadSerializer, PhoneFilterSerializer, PhoneShortSerializer


class PhoneViewSet(StorageAuthModelPaginateMixin):
    queryset = Phone.objects.all()
    serializer_class = PhoneReadSerializer
    filter_serializer = PhoneFilterSerializer
    filter_parse_query_params = (('date-create-from', 'date_create_from'),)
    serializer_map = {
        'create': PhoneWriteSerializer,
        'update': PhoneWriteSerializer,
    }


class PhoneShortViewSet(StorageAuthMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneShortSerializer
    filter_serializer = PhoneFilterSerializer
