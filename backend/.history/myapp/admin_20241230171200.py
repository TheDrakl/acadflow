from django.contrib import admin
from .models import Company, Role, UserRole, PricingPlans, PricingPlansFeatures

admin.site.register(PricingPlans)
admin.site.register(PricingPlansFeatures)
