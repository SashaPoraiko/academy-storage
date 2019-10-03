from rest_framework import routers

from .views import UserViewSet, PhoneViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'phone', PhoneViewSet)
