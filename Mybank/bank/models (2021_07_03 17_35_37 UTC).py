from django.db import models

# Create your models here.


class createAccount(models.Model):
    personname=models.CharField(max_length=120)
    accno=models.IntegerField()
    acctype=models.CharField(max_length=120)
    balance=models.IntegerField(default=3000)
    mpin=models.IntegerField()

    def __str__(self):
        return self.personname


class transferDetails(models.Model):
    accno=models.IntegerField()
    amount=models.IntegerField()
    mpin=models.IntegerField()

    def __str__(self):
        return self.accno+self.amount