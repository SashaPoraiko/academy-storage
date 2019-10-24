from rest_framework import routers

from .part.views import PartViewSet
from .phone.views import PhoneViewSet
from .phone_model.views import PhoneModelViewSet
from .storage.views import StorageViewSet
from . import views

router = routers.SimpleRouter()
router.register(r'users', views.UserViewSet)
router.register(r'phone', PhoneViewSet)
router.register(r'part', PartViewSet)
router.register(r'phone-model', PhoneModelViewSet)
router.register(r'storage', StorageViewSet)
