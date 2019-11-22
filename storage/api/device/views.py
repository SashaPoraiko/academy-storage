from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from storage.models import Device
from storage.api.views import StorageAuthMixin
from .serializers import DeviceReadSerializer


class DeviceViewSet(StorageAuthMixin, viewsets.ReadOnlyModelViewSet):
    queryset = Device.objects.all()
    serializer_class = DeviceReadSerializer
    permission_classes = (IsAuthenticated,)
