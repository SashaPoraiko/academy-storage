from rest_framework.permissions import IsAuthenticated

from ..views import StorageAuthModelPaginateMixin
from ..permissions import IsManager
from ..models import PhoneModel
from .serializers import PhoneModelSerializer, PhoneModelFilterSerializer


class PhoneModelViewSet(StorageAuthModelPaginateMixin):
    queryset = PhoneModel.objects.all()
    serializer_class = PhoneModelSerializer
    filter_serializer = PhoneModelFilterSerializer
    permission_classes = (IsAuthenticated, IsManager)
