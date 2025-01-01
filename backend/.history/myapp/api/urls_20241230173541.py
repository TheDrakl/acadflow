from django.urls import path
from .views import Prici


urlpatterns = [
    path('pricing/', PricingPlansList.as_view(), name='pricing-plans-list'),
]
