from rest_framework import viewsets, filters
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from django_filters.rest_framework import DjangoFilterBackend
from .models import Coupon
from .serializers import CouponSerializer
from django.http import HttpResponse

# Permission: Staff can create/update/delete, others read-only
class IsStaffOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_staff

class CouponViewSet(viewsets.ModelViewSet):
    queryset = Coupon.objects.all()
    serializer_class = CouponSerializer
    permission_classes = [IsAuthenticated, IsStaffOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'expiry_date']
    search_fields = ['code']

    def get_queryset(self):
        user = self.request.user
        if user.is_staff:
            return Coupon.objects.all()
        # Non-staff see only active coupons
        return Coupon.objects.filter(status='Active')
    
    
def index(request):
    return HttpResponse("Hello from coupons app!")

