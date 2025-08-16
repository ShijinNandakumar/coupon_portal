from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from coupons.views import CouponViewSet

router = DefaultRouter()
router.register(r'coupons', CouponViewSet, basename='coupon')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
