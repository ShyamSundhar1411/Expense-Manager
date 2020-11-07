from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Expense,Budget
from django.utils import timezone
from django.db import IntegrityError
from django.db.models import Sum
from django.contrib.auth.models import User
from django.utils.datastructures import MultiValueDictKeyError
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login,authenticate
from django.http import HttpResponse,Http404
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.forms import SetPasswordForm
from .forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
import csv
#Class Based Views
#Authentication
class Signup(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'
    def form_valid(self,form):
        v = super(Signup,self).form_valid(form)
        username, password = form.cleaned_data.get('username'),form.cleaned_data.get('password1')
        user = authenticate(username = username,password = password)
        login(self.request,user)
        return v

#CRUD
class Profile(LoginRequiredMixin,generic.UpdateView):
    model = User
    fields = ['username','email']
    success_url = reverse_lazy('profile')
    template_name = 'expense/updateprofile.html'
    def get_object(self,query_set = None):
        return self.request.user
class Update(LoginRequiredMixin,generic.UpdateView):
    model = Expense
    fields = ['title','expense','category','receipt','payment']
    template_name = 'expense/update.html'
    success_url = reverse_lazy('detail')
    def get_object(self):
        v = super(Update,self).get_object()
        if not v.expenser == self.request.user:
            raise Http404
        return v
class Upbud(LoginRequiredMixin,generic.UpdateView):
    model = Budget
    fields = ['budget','source']
    template_name = 'expense/upbud.html'
    success_url = reverse_lazy('detail')
    def get_object(self):
        v = super(Upbud,self).get_object()
        if not v.userin == self.request.user:
            raise Http404
        return v
class DelBud(LoginRequiredMixin,generic.DeleteView):
    model = Budget
    template_name = 'expense/deletebudget.html'
    success_url = reverse_lazy('budget')
    def get_object(self):
        v = super(DelBud,self).get_object()
        if not v.userin == self.request.user:
            raise Http404
        return v
class Delete(LoginRequiredMixin,generic.DeleteView):
    model = Expense
    template_name = 'expense/delete.html'
    success_url = reverse_lazy('detail')
    def get_object(self):
        v = super(Delete,self).get_object()
        if not v.expenser == self.request.user:
            raise Http404
        return v
#Function Based Views
def home(request):
    return render(request,'expense/home.html')
@login_required()
def add(request):
    if request.method=='POST':
        if request.POST['title'] and request.POST['expense'] and request.POST['category']  and request.POST['pay']:
            try:
                if request.FILES.get('receipt'):
                    im=request.FILES['receipt']
            except MultiValueDictKeyError:
                return render(request,'expense/add.html',{'error':'All fields are required'})
            exp=Expense()
            exp.title=request.POST['title']
            exp.expense=int(request.POST['expense'])
            exp.payment=request.POST['pay']
            exp.category=request.POST['category']
            exp.dot=timezone.datetime.now()
            if request.FILES.get('receipt'):
                exp.receipt = request.FILES['receipt']
            exp.expenser=request.user
            exp.save()
            return redirect('detail')
        else:
            return render(request,'expense/add.html',{'error':'All fields are required'})
    else:
        return render(request,'expense/add.html')
@login_required()
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
@login_required()
def detail(request):
    w = Expense.objects.filter(expenser=request.user).order_by('-dot')
    i = Budget.objects.filter(userin=request.user)
    if request.GET.get('filter') == 'Weekly':
        return render(request,'expense/detail.html',{'hey':w.order_by('-dot__week'),'bud':i})
    elif request.GET.get('filter') == 'Yearly':
        return render(request,'expense/detail.html',{'hey':w.order_by('-dot__year'),'bud':i})
    elif request.GET.get('filter') == 'Monthly':
        return render(request,'expense/detail.html',{'hey':w.order_by('-dot__month'),'bud':i})
    else:
        return render(request,'expense/detail.html',{'hey':w,'bud':i})
@login_required()
def analysis(request):
        w = Expense.objects.filter(expenser=request.user).order_by('-dot')
        z = Expense.objects.filter(expenser=request.user).aggregate(tot=Sum('expense'))
        i = Budget.objects.filter(userin=request.user)
        p = Budget.objects.filter(userin=request.user).aggregate(are=Sum('budget'))
        if p['are'] is None:
                return render(request,'expense/home.html',{'hey':w,'bud':i,'result':z,'error':'*Not enough Funds. Add Budget to Continue. Remember Your initial expense value will be deducted from the new Budget amount. Your Account is locked until that*'})
        elif z['tot'] is None:
                return render(request,'expense/home.html',{'hey':w,'bud':i,'result':z,'error':'*Enter Expense to continue. Your Account is locked until that*'})
        else:
            if z['tot']>p['are']:
                return render(request,'expense/home.html',{'hey':w,'bud':i,'result':z,'error':'*Not enough Funds. Add Budget to Continue. Remember Your initial expense value will be deducted from the new Budget amount. Your Account is locked until that*'})
            else:
                return render(request,'expense/analysis.html',{'hey':w,'bud':i,'result':z,'sue':p})
def about(request):
    return render(request,'expense/about.html')
def report(request):
    response = HttpResponse(content_type = 'text/csv')
    writer = csv.writer(response)
    if request.GET.get('repo') == 'Expense':
        writer.writerow(['Title','Category','Expense','Date','Mode of Payment'])
        for i in Expense.objects.filter(expenser = request.user).extra(select={'date':"STRFTIME('%%d-%%m-%%Y',dot)"}).values_list('title','category','expense','date','payment'):
            writer.writerow(i)
        response['Content-Disposition'] = 'attachment;filename = "Expense_reports.csv"'
        return response
    else:
        writer.writerow(['Budget','Source','Last Updated'])
        for i in Budget.objects.filter(userin= request.user).extra(select={'date':"STRFTIME('%%d-%%m-%%Y',dot)"}).values_list('budget','source','date'):
                writer.writerow(i)
        response['Content-Disposition'] = 'attachment;filename = "Budget_reports.csv"'
        return response
