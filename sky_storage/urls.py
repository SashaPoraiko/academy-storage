from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf.urls.static import static

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from sky_storage import settings

urlpatterns = [
    path('', include("storage.urls")),
    path('', include("management.urls")),
    path('admin/', admin.site.urls),
    path('api/auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
