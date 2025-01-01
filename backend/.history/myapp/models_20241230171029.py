from django.db import models
from django.conf import settings

class Company(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = ("Company")
        verbose_name_plural = ("Companies")

    def __str__(self):
        return self.name


class Role(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class UserRole(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    assigned_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'role', 'company')

    def __str__(self):
        return f'{self.user} with role {self.role} at {self.company}'
    

class PricingPlansFeatures(models.Model):
    


class PricingPlans(models.Model):
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    