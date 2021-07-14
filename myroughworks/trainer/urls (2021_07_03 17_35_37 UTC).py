

from django.contrib import admin
from django.urls import path
from trainer.views import trainerregistration,trainerlogin

urlpatterns = [
    path("trainerregistration",trainerregistration),
    path("trainerlogin",trainerlogin)

]
