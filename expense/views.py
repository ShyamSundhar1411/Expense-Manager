from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Expense,Budget
from django.utils import timezone
from django.db import IntegrityError
from django.db.models import Sum
from django.utils.datastructures import MultiValueDictKeyError
def home(request):
    p=Expense.objects
    return render(request,'expense/home.html',{'product':p})
def add(request):
    if request.method=='POST':
        if request.POST['title'] and request.POST['expense'] and request.POST['category']  and request.POST['pay']:
            try:
                im=request.FILES['receipt']
            except MultiValueDictKeyError:
                return render(request,'expense/add.html',{'error':'All fields are required'})
            exp=Expense()
            exp.title=request.POST['title']
            exp.expense=int(request.POST['expense'])
            exp.payment=request.POST['pay']
            exp.category=request.POST['category']
            exp.dot=timezone.datetime.now()
            exp.expenser=request.user
            exp.receipt=request.FILES['receipt']
            exp.save()
            return redirect('detail')
        else:
            return render(request,'expense/add.html',{'error':'All fields are required'})
    else:
        return render(request,'expense/add.html')
def budget(request):
    if request.method=='POST':
        if request.POST['budget']:
            exp=Budget()
            exp.userin=request.user
            exp.budget=int(request.POST['budget'])
            exp.dot=timezone.datetime.now()
            exp.source=request.POST['source']
            exp.save()
            k=Budget.objects
            return render(request,'expense/home.html',{'budget':'Successfully Added ${x} to your account'.format(x=exp.budget)})
        else:
            return render(request,'expense/budget.html',{'error':'Entered the required fields'})
    else:
        return render(request,'expense/budget.html')
def detail(request):
        w=Expense.objects.filter(expenser=request.user)
        z=Expense.objects.filter(expenser=request.user).aggregate(tot=Sum('expense'))
        i=Budget.objects.filter(userin=request.user)
        p=Budget.objects.filter(userin=request.user).aggregate(are=Sum('budget'))
        if p['are'] is None:
                return render(request,'expense/home.html',{'hey':w,'bud':i,'result':z,'error':'*Not enough Funds. Add Budget to Continue. Remember Your initial expense value will be deducted from the new Budget amount. Your Account is locked until that*'})
        elif z['tot'] is None:
                return render(request,'expense/home.html',{'hey':w,'bud':i,'result':z,'error':'*Enter Expense to continue. Your Account is locked until that*'})

        else:
            if z['tot']>p['are']:
                return render(request,'expense/home.html',{'hey':w,'bud':i,'result':z,'error':'*Not enough Funds. Add Budget to Continue. Remember Your initial expense value will be deducted from the new Budget amount. Your Account is locked until that*'})
            else:
                return render(request,'expense/detail.html',{'hey':w,'bud':i,'result':z,'sue':p})
def about(request):
    return render(request,'expense/about.html')
