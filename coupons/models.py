from django.db import models

class Coupon(models.Model):
    STATUS_CHOICES = [
        ('Active', 'Active'),
        ('Consumed', 'Consumed'),
        ('Expired', 'Expired'),
    ]

    code = models.CharField(max_length=50, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Active')
    expiry_date = models.DateTimeField()
    consumed_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.code
