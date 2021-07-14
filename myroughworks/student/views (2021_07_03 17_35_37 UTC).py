from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def studRegistration(request):
    return HttpResponse("<h1> welcome to student registration</h1>")
def studlogin(request):
    return HttpResponse("<h1> welcome to login page</h1>")


