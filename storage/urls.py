from rest_framework import routers

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
