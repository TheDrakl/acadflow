from ..models import PricingPlans
from rest_framework import serializers

class PricingPlansSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingPlans
        fields = '__all__'