from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Expense,Budget
from django.utils import timezone


def home(request):
    return render(request,'expense/home.html')
def add(request):
    if request.method=='POST':
        if request.POST['title'] and request.POST['expense'] and request.POST['category']:
            exp=Expense()
            exp.title=request.POST['title']
            exp.expense=request.POST['expense']
            exp.category=request.POST['category']
            exp.dot=timezone.datetime.now()
            exp.expenser=request.user
            exp.save()
            return redirect('/expense/'+ str(exp.id),)

    else:
        return render(request,'expense/add.html')
def budget(request):
    if request.method=='POST':
        budget=Budget()
        if budget.budget==0:

            budget.budget=request.POST['budget']
        else:
            budget.budget+=request.POST['budget']
    else:
        return render(request,'expense/budget.html')
def detail(request,expense_id):
        a=get_object_or_404(Expense, pk = expense_id)
        w=Expense.objects.all()
        return render(request,'expense/detail.html',{'expense':a,'hey':w})
