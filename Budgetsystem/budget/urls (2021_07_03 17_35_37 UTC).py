"""Budgetsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from budget.views import register,loginView,signOut,editProfile,userHome,addExpenses,editExpense,deleteExpense,review_expense,index
urlpatterns = [
    path("",index,name="index"),
    path("register/",register,name="register"),
    path("login/",loginView,name="login"),
    path("logout/",signOut,name="logout"),
    path("edit/",editProfile,name="edit"),
    path("home/",userHome,name="home"),
    path("addexpens/",addExpenses,name="addexpens"),
    path("editexpens/<int:id>",editExpense,name="editexpens"),
    path("delete/<int:id>",deleteExpense,name="delete"),
    path("reviewexp/",review_expense,name="reviewexp"),
]
