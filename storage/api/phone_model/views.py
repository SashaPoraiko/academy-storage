from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from storage.api.views import StorageAuthModelPaginateMixin, StorageAuthMixin
from storage.permissions import IsManager
from storage.models import PhoneModel
from .serializers import PhoneModelSerializer, PhoneModelFilterSerializer, PhoneModelShortSerializer


class PhoneModelViewSet(StorageAuthModelPaginateMixin):
    queryset = PhoneModel.objects.all()
    serializer_class = PhoneModelSerializer
    filter_serializer = PhoneModelFilterSerializer
    permission_classes = (IsAuthenticated, IsManager)


class PhoneModelShortViewSet(StorageAuthMixin, viewsets.ReadOnlyModelViewSet):
    queryset = PhoneModel.objects.all()
    serializer_class = PhoneModelShortSerializer
    filter_serializer = PhoneModelFilterSerializer
