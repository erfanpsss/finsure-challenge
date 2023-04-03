from django.contrib import admin
from .models import Lender

@admin.register(Lender)
class LenderAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "code", "upfront_commission_rate", "trial_commission_rate", "active"]
