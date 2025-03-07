from django.db import models
from django.conf import settings


class PricingPlansFeatures(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PricingPlans(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.ManyToManyField(PricingPlansFeatures)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def __str__(self):
        return self.
    

    