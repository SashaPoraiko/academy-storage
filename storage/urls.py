from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'phone', views.PhoneViewSet)
router.register(r'part', views.PartViewSet)
router.register(r'phone-model', views.PhoneModelViewSet)
router.register(r'storage', views.StorageViewSet)
