from django.forms import ModelForm
from  django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from budget.models import Expenses

from budget.models import loginView


class RegistrationForm(UserCreationForm):
    class Meta:
        model=User
        fields=["first_name","last_name","email","username","password1","password2"]

class LoginViewForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField()

    def clean(self):
        cleaned_data=super().clean()
        username=cleaned_data.get("username")
        password=cleaned_data.get("password")
        print(username,",",password)
        # try:
        #     object=.objects.get(username=username)
        #     if object:
        #         pass
        # except:
        #         msg="invalid username"
        #         self.add_error("username",msg)
        # try:
        #     object=RegistrationForm.objects.get(password=password)
        #     if object:
        #         pass
        # except:
        #         msg="invalid password"
        #         self.add_error("password",msg)


class AddExpenseForm(ModelForm):
    user= forms.CharField(widget=forms.TextInput(attrs={'readonly':'readonly'}))
    class Meta:
        model=Expenses
        fields=["category","amount","note","user"]


class ReviewExpenseForm(forms.Form):
    user=forms.HiddenInput()
    from_date=forms.DateField(widget=forms.SelectDateWidget())
    to_date=forms.DateField(widget=forms.SelectDateWidget())