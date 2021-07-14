from django.contrib import admin
from budget.models import Category,Expenses


# Register your models here.
admin.site.register(Category)
admin.site.register(Expenses)

# superuser:name:budget
# password=budget
# name=maria
