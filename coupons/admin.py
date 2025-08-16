from django.contrib import admin
from .models import Coupon

class CouponAdmin(admin.ModelAdmin):
    list_display = ('code', 'status', 'expiry_date', 'consumed_date')
    list_filter = ('status',)
    search_fields = ('code',)

    # Only staff can add
    def has_add_permission(self, request):
        return request.user.is_staff

    # Only staff can edit
    def has_change_permission(self, request, obj=None):
        return request.user.is_staff

    # Only staff can delete
    def has_delete_permission(self, request, obj=None):
        return request.user.is_staff

    # Non-staff users can only see active coupons
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_staff:
            return qs
        return qs.filter(status='Active')

admin.site.register(Coupon, CouponAdmin)
