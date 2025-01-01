from ..models import PricingPlan
from rest_framework import serializers

class PricingPlan

class PricingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingPlan
        fields = '__all__'