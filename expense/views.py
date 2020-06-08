from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Expense,Budget
from django.utils import timezone
from django.db import IntegrityError

def home(request):
    p=Expense.objects
    return render(request,'expense/home.html',{'product':p})
def add(request):
    if request.method=='POST':
        if request.POST['title'] and request.POST['expense'] and request.POST['category'] and request.FILES['receipt']:
            exp=Expense()
            exp.title=request.POST['title']
            exp.expense=request.POST['expense']
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
            exp.budget=request.POST['budget']
            exp.dot=timezone.datetime.now()
            exp.save()
            k=Budget.objects
            return render(request,'expense/home.html',{'budget':'Successfully Added {x} to your account'.format(x=exp.budget)})
        else:
            return render(request,'expense/budget.html',{'error':'Entered the required fields'})
    else:
        return render(request,'expense/budget.html')
def detail(request):
        w=Expense.objects.filter(expenser=request.user)
        i=Budget.objects.filter(userin=request.user)
        return render(request,'expense/detail.html',{'hey':w,'bud':i})
def about(request):
    return render(request,'expense/about.html')
