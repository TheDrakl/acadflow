from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import generics
from .models import PricingPlan



class PricingPlansList(generics.ListCreateAPIView):
    queryset = PricingPlan.objects.all()
    serializer_class = PricingPlanSerializer
