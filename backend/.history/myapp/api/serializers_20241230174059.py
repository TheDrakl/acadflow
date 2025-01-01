from ..models import PricingPlan, PricingPlanFeature
from rest_framework import serializers

class PricingPlanFeatureSeializer(serializers.ModelSerializer):
    class Meta:
        model = PricingPlanFeature
        fields = ['id', 'name']

class PricingPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = PricingPlan
        fields = '__all__'