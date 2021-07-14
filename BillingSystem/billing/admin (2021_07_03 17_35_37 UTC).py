from django.contrib import admin

# Register your models here.
from billing.models import Products,Purchase

admin.site.register(Purchase)
admin.site.register(Products)

