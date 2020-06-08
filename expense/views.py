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
            return redirect('/expense/'+ str(exp.id))
        else:
            return render(request,'expense/add.html',{'error':'All fields are required'})
    else:
        return render(request,'expense/add.html')
def budget(request):
    if request.method=='POST':
        exp=Budget()
        exp.userin=request.user
        exp.budget=request.POST['budget']
        exp.budl(request.GET['expense'])
        exp.save()
        k=Budget.objects
        return render(request,'expense/home.html',{'budget':k})
    else:
        return render(request,'expense/budget.html')
def detail(request,expense_id):
        a=get_object_or_404(Expense, pk = expense_id)
        a.save()
        w=Expense.objects.filter(expenser=request.user)
        i=Budget.objects.filter(userin=request.user)
        g=len(a.title)
        return render(request,'expense/detail.html',{'expe':a,'hey':w,'bud':i,'Transactions':g})
def about(request):
    return render(request,'expense/about.html')
