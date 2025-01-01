from django.urls import path
from .views import PricingPlansList


urlpatterns = [
    path('pricing/', PricingPlansList.as_view(), name='pricing-plans-list'),
]
