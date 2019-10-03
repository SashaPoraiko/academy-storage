from rest_framework import routers

from storage.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
