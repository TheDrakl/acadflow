from django.contrib import admin
from .models import Company, Role, UserRole

admin.site.register(Company)
admin.site.register(Role)
admin.site.register(UserRole)