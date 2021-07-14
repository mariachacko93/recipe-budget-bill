from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def trainerregistration(request):
    return render(request,"trainer/trainerreg.html")

def trainerlogin(request):
    return render(request,"trainer/trainerlogin.html")

