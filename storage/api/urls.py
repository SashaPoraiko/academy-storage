from django.conf.urls import url
from rest_framework import routers

from .device.views import DeviceViewSet
from .profile.views import ProfileView, ForgotPasswordView, ResetPasswordView, UserViewSet
from .part.views import PartViewSet, PartShortViewSet
from .phone.views import PhoneViewSet, PhoneShortViewSet
from .phone_model.views import PhoneModelViewSet, PhoneModelShortViewSet
from .storage.views import StorageViewSet, StorageShortViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

router.register(r'phone/short', PhoneShortViewSet)
router.register(r'phone', PhoneViewSet)

router.register(r'part/short', PartShortViewSet)
router.register(r'part', PartViewSet)

router.register(r'phone_model/short', PhoneModelShortViewSet)
router.register(r'phone_model', PhoneModelViewSet)

router.register(r'storage/short', StorageShortViewSet)
router.register(r'storage', StorageViewSet)

router.register(r'device', DeviceViewSet)

urlpatterns = [
    url(r'profile', ProfileView.as_view()),
    url(r'password/forgot', ForgotPasswordView.as_view()),
    url(r'password/reset', ResetPasswordView.as_view()),
]
urlpatterns += router.urls
