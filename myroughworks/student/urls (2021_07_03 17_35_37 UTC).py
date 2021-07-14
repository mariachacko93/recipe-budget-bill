


from django.contrib import admin
from django.urls import path
from student.views import studRegistration,studlogin


urlpatterns = [

 path("studentregistration",studRegistration),
 path("studlogin",studlogin),
]
