from rest_framework import viewsets

from ..models import PhoneModel
from .serializers import PhoneModelSerializer


class PhoneModelViewSet(viewsets.ModelViewSet):
    queryset = PhoneModel.objects.all()
    serializer_class = PhoneModelSerializer

    def get_queryset(self):
        name = self.request.query_params.get('name')
        if name:
            self.queryset = self.queryset.filter(name__icontains=name)
        brand = self.request.query_params.get('brand')
        if brand:
            self.queryset = self.queryset.filter(brand__icontains=brand)

        return self.queryset
