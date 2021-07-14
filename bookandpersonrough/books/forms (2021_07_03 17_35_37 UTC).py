from django import forms

class BookCreateForm(forms.Form):
    bookname=forms.CharField()
    price=forms.IntegerField()
    pages=forms.IntegerField()
    author=forms.CharField()
