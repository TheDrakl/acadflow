from django.db import models
from django.conf import settings


class PricingPlanFeature(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class PricingPlan(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    features = models.ManyToManyField(PricingPlanFeature)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    mostSold = models.BooleanField(default=False)

    def __str__(self):
        return self.name + ' - $' + str(self.price)
    

    