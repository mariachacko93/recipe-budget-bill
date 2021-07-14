from django.shortcuts import render,redirect
from budget.forms import LoginViewForm
from budget.models import Expenses
# Create your views here.
from budget.forms import RegistrationForm,AddExpenseForm,ReviewExpenseForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.db.models import Sum,Aggregate
from django.contrib.auth.decorators import login_required


# username-zayn
# password-Zayn12345

def index(request):
    return render(request,"budget/index.html")

def register(request):
    form=RegistrationForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,"budget/home.html", context)
        else:
            context["form"]=form
            return render(request,"budget/register.html",context)
    else:
        context["form"]=form
        return render(request, "budget/register.html", context)


def loginView(request):
    form=LoginViewForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=LoginViewForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            password=form.cleaned_data.get("password")
            user=authenticate(request,username=username,password=password)
            if user:
                login(request,user)

                return render(request, "budget/home.html", context)
            else:
                context["form"]=form
                return render(request, "budget/login.html", context)
        else:
            context["form"] = form
            return render(request, "budget/login.html", context)

    return render(request,"budget/login.html",context)

def signOut(request):
    logout(request)
    return redirect("login")

@login_required
def editProfile(request):
    user=User.objects.get(username=request.user)
    form=RegistrationForm(instance=user)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=RegistrationForm(instance=user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            context["form"]=form
            return render(request, "budget/editprofile.html", context)

    return render(request,"budget/editprofile.html",context)

@login_required
def userHome(request):
    return render(request, "budget/home.html")

@login_required
def addExpenses(request):
    form=AddExpenseForm(initial={"user":request.user})
    context={}
    context["form"]=form
    expenses=Expenses.objects.filter(user=request.user)
    context["expenses"]=expenses
    print(expenses)
    if request.method=="POST":
        form=AddExpenseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("addexpens")
        else:
            context["form"]=form
            return render(request,"budget/addexpens.html",context)
    return render(request,"budget/addexpens.html",context)

@login_required
def editExpense(request,id):
    expense=Expenses.objects.get(id=id)
    form=AddExpenseForm(instance=expense)
    context={}
    context["form"]=form
    if request.method=="POST":
        form=AddExpenseForm(instance=expense,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("addexpens")
        else:
            context["form"]=form
            return render(request,"budget/editexpens.html",context)
    return render(request,"budget/editexpens.html",context)

@login_required
def deleteExpense(request,id):
    try:
        Expenses.objects.get(id=id).delete()
        return redirect("addexpens")
    except Exception as e:
        return redirect("addexpens")

@login_required
def review_expense(request):
    form=ReviewExpenseForm(initial={"user":request.user})
    context={}
    context["form"]=form
    if request.method=="POST":
        form=ReviewExpenseForm(request.POST)
        if form.is_valid():
            fromdate=form.cleaned_data.get("from_date")
            todate=form.cleaned_data.get("to_date")
            print(fromdate,",",todate)

            expenses=Expenses.objects.filter(date__gte=fromdate,date__lte=todate,user=request.user)
            total=Expenses.objects.filter(date__gte=fromdate,date__lte=todate,user=request.user).aggregate(Sum("amount"))

            context["total"]=total
            context["expenses"]=expenses
        # else:
        #     context["form" ]=form
            return render(request, "budget/reviewexp.html", context)

    return render(request,"budget/reviewexp.html",context)
