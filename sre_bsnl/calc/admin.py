from django.contrib import admin
from .models import Customers, Plan

# Register your models here.
admin.site.register(Customers)
admin.site.register(Plan)