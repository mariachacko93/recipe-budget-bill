from django.db import models
from django.forms import ModelForm
# Create your models here.

class loginView(models.Model):
    username=models.CharField(max_length=120)
    password=models.CharField(max_length=120)

    def __str__(self):
        return self.username


class Category(models.Model):
    categoryname=models.CharField(max_length=120,unique=True)

    def __str__(self):
        return self.categoryname

class Expenses(models.Model):
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    amount=models.IntegerField()
    date=models.DateField(auto_now=True)
    note=models.CharField(max_length=120)
    user=models.CharField(max_length=120)


    def __str__(self):
            return self.user



