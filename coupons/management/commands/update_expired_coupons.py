from django.core.management.base import BaseCommand
from coupons.models import Coupon
from django.utils import timezone

class Command(BaseCommand):
    help = 'Updates coupon status to Expired if past expiry date.'

    def handle(self, *args, **kwargs):
        now = timezone.now()
        expired_coupons = Coupon.objects.filter(expiry_date__lt=now, status='Active')

        for coupon in expired_coupons:
            coupon.status = 'Expired'
            coupon.save()
            self.stdout.write(self.style.SUCCESS(f'Coupon {coupon.code} marked as Expired.'))

        if not expired_coupons.exists():
            self.stdout.write(self.style.WARNING('No coupons needed updating.'))
