from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from ..models import PricingPlan
from .serializers import PricingPlanSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework_simplejwt.authentication import JWTAuthentication



class PricingPlansList(generics.ListCreateAPIView):
    queryset = PricingPlan.objects.all()
    serializer_class = PricingPlanSerializer
    authentication_classes = [JWTAuthentication]  # JWTAuthentication for handling JWT tokens

