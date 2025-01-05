from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import generics
from .models import PricingPlan
from .serializers import PricingPlanSerializer

class PricingPlansList(generics.ListCreateAPIView):
    queryset = PricingPlan.objects.all()
    serializer_class = PricingPlanSerializer
    authentication_classes = [JWTAuthentication]  # JWTAuthentication for handling JWT tokens
    permission_classes = [IsAuthenticated]  # Ensures the user is authenticated