from django.contrib.auth.models import User

from rest_framework import viewsets

from .models import Phone
from .serializers import UserSerializer, PhoneSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class PhoneViewSet(viewsets.ModelViewSet):
    queryset = Phone.objects.all()
    serializer_class = PhoneSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        comment = self.request.query_params.get('comment', None)
        if comment is not None:
            self.queryset = self.queryset.filter(comment__icontains=comment)

        phone_model = self.request.query_params.get('phone-model', None)
        if phone_model is not None:
            self.queryset = self.queryset.filter(phone_model=phone_model)

        date_create_from = self.request.query_params.get('date-create-from', None)
        date_create_to = self.request.query_params.get('date-create-to', None)

        if date_create_from and date_create_to:
            self.queryset = self.queryset.filter(date_create__range=[date_create_from, date_create_to])
        else:
            if date_create_from:
                self.queryset = self.queryset.filter(date_create__gte=date_create_from)

            if date_create_to:
                self.queryset = self.queryset.filter(date_create__lte=date_create_to)


        return self.queryset