from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.exceptions import ValidationError
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode

from rest_framework.exceptions import PermissionDenied
from rest_framework.generics import RetrieveUpdateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.authentication import JWTAuthentication

from sky_storage.settings import HOST, STATIC_URL
from .serializers import ForgotPasswordSerializer, ValidatePasswordSerializer
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

    def post(self, request):
        validator = self.serializer_class(data=request.data)
        validator.is_valid(raise_exception=True)
        user = User.objects.filter(is_active=True, email=validator.validated_data['email']).first()

        if user:
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = default_token_generator.make_token(user)
            context = {
                'uid': uid,
                'token': token,
                'host': HOST,
                'url': ''.join((HOST, '/api/v1/password/reset/?uid=', uid, '&token=', token)),
                'logo_url': ''.join((HOST, STATIC_URL, 'images/monkey.png'))
            }
            text_content = f'Change password below, copy and paste the following link in your browser: {context["url"]}'
            html_content = render_to_string('emails/forgot-password.html', context)
            msg = EmailMultiAlternatives('Forgot Password', text_content, 'Poraiko Alexandr', [user.email])
            msg.attach_alternative(html_content, "text/html")
            msg.send()
        return Response({
            'status': 'DELIVERY'
        })


class ResetPasswordView(APIView):
    user = None

    @classmethod
    def get_user(cls, uid, token):
        try:
            user = User.objects.get(pk=urlsafe_base64_decode(uid))
        except (TypeError, ValueError, OverflowError, ValidationError, User.DoesNotExist):
            return None
        is_valid = default_token_generator.check_token(user, token)
        return user if is_valid else None

    def initial(self, request, *args, **kwargs):
        super().initial(request, args, kwargs)
        uid = request.query_params.get('uid', '')
        token = request.query_params.get('token', '')
        self.user = self.get_user(uid, token)
        if self.user is None:
            raise PermissionDenied

    def get(self, request):
        return Response(UserSerializer(instance=self.user).data)

    def post(self, request):
        validator = ValidatePasswordSerializer(data=request.data, context={'user': self.user})
        validator.is_valid(raise_exception=True)
        self.user.set_password(validator.validated_data['password'])
        self.user.save()
        return Response({'status': 'Successfully'})
