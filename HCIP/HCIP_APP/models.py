from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import random
from decimal import Decimal

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    PENDING = 'pending'
    APPROVED = 'approved'
    FAILED = 'failed'

    STATUS_CHOICES = [
        (PENDING, 'Pending'),
        (APPROVED, 'Approved'),
        (FAILED, 'Failed'),
    ]

    amount = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)
    proposed_amount = models.DecimalField(max_digits=50, decimal_places=2, default=0.00)
    date = models.DateField(default=timezone.now)
    payment_status = models.CharField(max_length=10, choices=STATUS_CHOICES, default=PENDING)
    profit = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, default=0.00)
    otp = models.CharField(max_length=4, blank=True)

    def calculate_profit(self):
        if self.amount:
            return self.amount * Decimal('50.00')  # Corrected calculation to 5% of amount
        return Decimal('0.00')

    def generate_otp(self):
        self.otp = ''.join(random.choices('0123456789', k=4))

    def __str__(self):
        return self.user.username
