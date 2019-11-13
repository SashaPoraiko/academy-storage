from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateAPIView

from django.contrib.auth.models import User
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from .serializers import ForgotPasswordSerializer
from ..serializers import UserSerializer


class ProfileView(RetrieveUpdateAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = UserSerializer
    queryset = User.objects.filter(is_active=True)
    user = None

    def initial(self, request, *args, **kwargs):
        super().initial(request, args, kwargs)
        self.user = request.user

    def get_queryset(self):
        return self.queryset.filter(pk=self.user.id)

    def get_object(self):
        return self.user


class ForgotPasswordView(APIView):
    serializer_class = ForgotPasswordSerializer

    # queryset = User.objects.filter(is_active=True)

    def post(self, request):
        validator = self.serializer_class(data=request.data)
        validator.is_valid(raise_exception=True)
        user = User.objects.filter(is_active=True, email=validator.validated_data['email']).first()
        if user:
            d = {'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            'token': PasswordResetTokenGenerator().make_token(user)
                 }
            # todo send email to user
            return Response(d)
        return Response({
            'status': 'DELIVERY'
        })
