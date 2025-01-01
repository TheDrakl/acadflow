from django.urls import path
urlpatterns = [
    path('pricing/', PricingPlansList.as_view(), name='pricing-plans-list'),
]
