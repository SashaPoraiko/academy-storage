from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from ..views import StorageAuthModelPaginateMixin, StorageAuthMixin
from ..models import  Device
from .serializers import DeviceReadSerializer


class DeviceViewSet(StorageAuthMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceReadSerializer
    permission_classes = (IsAuthenticated,)
