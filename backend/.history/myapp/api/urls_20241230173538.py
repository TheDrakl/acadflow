from django.urls import path
from


urlpatterns = [
    path('pricing/', PricingPlansList.as_view(), name='pricing-plans-list'),
]
