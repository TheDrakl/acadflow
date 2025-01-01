from django.contrib import admin
from .models import PricingPlans, PricingPlansFeatures

admin.site.register(PricingPlan)
admin.site.register(PricingPlansFeature)
