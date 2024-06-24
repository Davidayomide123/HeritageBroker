# admin.py

from .models import *

from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'amount', 'date', 'payment_status', 'profit', 'otp')
    list_filter = ('payment_status',)
    search_fields = ('user__username', 'email', 'phone_number')
    readonly_fields = ('date', 'profit', 'otp', 'proposed_amount')

admin.site.register(UserProfile, UserProfileAdmin)

