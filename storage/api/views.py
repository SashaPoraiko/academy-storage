from django.conf import settings
from django.shortcuts import render

from rest_framework import viewsets, views
from rest_framework.authentication import SessionAuthentication
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from storage.api.utils import parse_query_params


AUTHENTICATION_CLASSES = (JWTAuthentication, SessionAuthentication) if settings.DEBUG else (JWTAuthentication,)


class StoragePagination(PageNumberPagination):
    page_size = 10
    max_page_size = 1000
    page_size_query_param = 'page-size'


class AuthMixin(viewsets.GenericViewSet):
    authentication_classes = AUTHENTICATION_CLASSES
    permission_classes = (IsAuthenticated,)


class PaginateMixin(viewsets.GenericViewSet):
    pagination_class = StoragePagination


class StorageMixin(viewsets.GenericViewSet):
    def get_queryset(self):
        queryset = super().get_queryset()
        filter_serializer = getattr(self, 'filter_serializer', None)

        if filter_serializer is None:
            return queryset

        data = parse_query_params(
            self.request.query_params,
            getattr(self, 'filter_parse_query_params', None)
        )

        filter_serializer = filter_serializer(data=data, context={'request': self.request})
        if filter_serializer.is_valid():
            return queryset.filter(**filter_serializer.validated_data)

        return queryset

    def get_serializer_class(self):
        serializer_class = super().get_serializer_class()
        serializer_map = getattr(self, 'serializer_map', {})
        return serializer_map.get(self.action, serializer_class)


class StorageModelMixin(StorageMixin, viewsets.ModelViewSet):
    pass


class StoragePaginateMixin(StorageMixin, PaginateMixin):
    pass


class StorageModelPaginateMixin(PaginateMixin, StorageModelMixin):
    pass


class StorageAuthMixin(StorageMixin, AuthMixin):
    pass


class StorageAuthModelMixin(AuthMixin, StorageModelMixin):
    pass


class StorageAuthPaginateMixin(StorageAuthMixin, StoragePaginateMixin):
    pass


class StorageAuthModelPaginateMixin(StorageAuthModelMixin, PaginateMixin):
    pass


class IndexView(views.APIView):

    def get(self, request):
        return render(request, 'emails/forgot-password.html')
