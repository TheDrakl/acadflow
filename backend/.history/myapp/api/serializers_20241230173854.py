from ..models import PricingPlan, PricingPlansFeature
from rest_framework import serializers

class PricingPlanFeatureSeializer(serializers.ModelSerializer):
    class Meta:
        model = PricingPlanFeature
        fields = '__all__'

class PricingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingPlan
        fields = '__all__'