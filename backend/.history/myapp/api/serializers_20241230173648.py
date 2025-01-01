from ..models import PricingPlan
from rest_framework import serializers

class PricingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingPlan
        fields = '__all__'