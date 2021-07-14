from django.shortcuts import render,redirect
from bank.forms import BankAccountForm,LoginViewForm,BalanceEnqForm,AccountActivityForm
from bank.models import createAccount

# Create your views her.
# from django.http import HttpResponse
def Transfer(request):
    form=AccountActivityForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=AccountActivityForm(request.POST)
        if form.is_valid():
            mpin=form.cleaned_data.get("mpin")
            amount=form.cleaned_data.get("amount")
            try:
                object=createAccount.objects.get(mpin=mpin)
                bal=object.balance-amount
                object.balance=bal
                object.save()
            except:
                print("invalid user")
                context["form"]=form
                return render(request,"bank/transfer.html",context)

            return redirect("balance")
        else:
            context["form"]=form
            return render(request,"bank/transfer.html",context)

    return render(request,"bank/transfer.html",context)

def CreateAccount(request):
    form=BankAccountForm
    context={}
    context["form"]=form
    if (request.method=="POST"):
        form=BankAccountForm(request.POST)
        if form.is_valid():
            personname=form.cleaned_data.get("personname")
            accno=form.cleaned_data.get("accno")
            acctype=form.cleaned_data.get("acctype")
            balance=form.cleaned_data.get("balance")
            mpin=form.cleaned_data.get("mpin")

            print(personname,",",accno,",",acctype,",",balance,",",mpin)
            account=createAccount(personname=personname,accno=accno,acctype=acctype,balance=balance,mpin=mpin)

            account.save()
            return redirect("list")

    return render(request,"bank/bank.html",context)



def AccList(request):
    account=createAccount.objects.all()
    context={}
    context["account"]=account
    return render(request,"bank/list.html",context)


def LoginView(request):
    form=LoginViewForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=LoginViewForm(request.POST)
        if form.is_valid():
            personname=form.cleaned_data.get("personname")
            mpin=form.cleaned_data.get("mpin")
            print(personname,",",mpin)
            try:
                object=createAccount.objects.get(personname=personname)
                if((object.personname==personname & object.mpin==mpin)):
                    print("user exists")
                    return render(request,"bank/bank.html")
            except Exception as e:
                print("invalid user")
                context["form"]=form
                return render(request, "bank/login.html", context)

    return render(request,"bank/login.html",context)

def balanceEnq(request):
    form=BalanceEnqForm()
    context={}
    context["form"]=form
    if request.method=="POST":
        form=BalanceEnqForm(request.POST)
        if form.is_valid():
            mpin=form.cleaned_data.get("mpin")
            try:
                account=createAccount.objects.get(mpin=mpin)
                context["balance"]=account.balance
                return render(request,"bank/balance.html",context)
            except Exception as e:
                print("user invalid")
                return render(request,"bank/balance.html",context)

    return render(request,"bank/balance.html",context)

