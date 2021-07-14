from django import forms
from bank.models import createAccount,transferDetails
from django.forms import ModelForm

class BankAccountForm(forms.Form):
    personname=forms.CharField(max_length=120)
    accno=forms.IntegerField()
    acctype=forms.CharField(max_length=120)
    balance=forms.IntegerField()
    mpin=forms.IntegerField()

class LoginViewForm(forms.Form):
    phonenumber=forms.IntegerField()
    mpin=forms.CharField(max_length=12)

class BalanceEnqForm(forms.Form):
    mpin=forms.CharField(max_length=120)

class AccountActivityForm(ModelForm):
    class Meta:
        model=transferDetails
        fields="__all__"
    def clean(self):
        cleaned_data=super().clean()
        mpin=cleaned_data.get("mpin")
        accno=cleaned_data.get("accno")
        amount=cleaned_data.get("amount")
        print(mpin,",",accno,",",amount)
        try:
            object=createAccount.objects.get(mpin=mpin)
            if (object):
                if (object.balance<amount):
                    print("insufficent amount")
                    msg="insufficent amount"
                    self.add_error("amount",msg)
                pass
        except:
            print("invalid pin")
            msg="invalid pin"
            self.add_error("mpin",msg)
        try:
            object=createAccount.objects.get(accno=accno)
            if object:
                pass
        except:
            print("invalid accno")
            msg = "invalid accno"
            self.add_error("accno",msg)


