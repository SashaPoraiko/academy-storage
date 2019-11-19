from django.conf.urls import url
from rest_framework import routers

from .device.views import DeviceViewSet
from storage.profile.views import ProfileView, ForgotPasswordView, ResetPasswordView
from .part.views import PartViewSet, PartShortViewSet
from .phone.views import PhoneViewSet, PhoneShortViewSet
from .phone_model.views import PhoneModelViewSet, PhoneModelShortViewSet
from .storage.views import StorageViewSet, StorageShortViewSet
from . import views

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet)

router.register(r'phone/short', PhoneShortViewSet)
router.register(r'phone', PhoneViewSet)

router.register(r'part/short', PartShortViewSet)
router.register(r'part', PartViewSet)

router.register(r'phone-model/short', PhoneModelShortViewSet)
router.register(r'phone-model', PhoneModelViewSet)

router.register(r'storage/short', StorageShortViewSet)
router.register(r'storage', StorageViewSet)

router.register(r'device', DeviceViewSet)

urlpatterns = [
    url(r'profile', ProfileView.as_view()),
    url(r'password/forgot', ForgotPasswordView.as_view()),
    url(r'password/reset', ResetPasswordView.as_view()),
]
urlpatterns += router.urls
