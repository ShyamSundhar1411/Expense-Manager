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
from django.http import HttpResponse,Http404,JsonResponse
from django.urls import reverse_lazy
from django.views import generic
from .filters import ExpenseFilter,BudgetFilter
from .forms import UserCreationForm,ExpenseCreationForm,BudgetCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
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
    fields = ['budget','source','category']
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
    success_url = reverse_lazy('detail')
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
#Filterers
class ExpenseCategoriser(LoginRequiredMixin,generic.ListView):
    model = Expense
    template_name = 'expense/expensecategoriser.html'
    def get_queryset(self):
        return Expense.objects.filter(expenser = self.request.user)
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['filterer'] = ExpenseFilter(self.request.GET,queryset = self.get_queryset())
        return context
class BudgetCategoriser(LoginRequiredMixin,generic.ListView):
    model = Budget
    template_name = 'expense/budgetcategoriser.html'
    def get_queryset(self):
        return Budget.objects.filter(userin = self.request.user)
    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['filterer'] = BudgetFilter(self.request.GET,queryset = self.get_queryset())
        return context
#Function Based Views
def home(request):
    return render(request,'expense/home.html')
@login_required()
def add(request):
    if request.method=='POST':
        try:
            form = ExpenseCreationForm(request.POST,request.FILES)
            newform = form.save(commit=False)
            newform.expenser = request.user
            newform.save()
            return redirect('detail')
        except ValueError:
            return render(request, 'expense/add.html', {'form':ExpenseCreationForm(), 'error': messages.error(request,'Bad data passed in. Try again.')})

    else:
        return render(request,'expense/add.html',{'form':ExpenseCreationForm()})
@login_required()
def budget(request):
        if request.method=='POST':
            try:
                form = BudgetCreationForm(request.POST)
                newform = form.save(commit=False)
                newform.userin = request.user
                newform.save()
                return redirect('detail')
            except ValueError:
                return render(request, 'expense/budget.html', {'form':BudgetCreationForm(), 'error': messages.error(request,'Bad data passed in. Try again.')})

        else:
            return render(request,'expense/budget.html',{'form':BudgetCreationForm()})
@login_required()
def detail(request):
    w = Expense.objects.filter(expenser=request.user).order_by('-dot')
    i = Budget.objects.filter(userin=request.user)
    totalbudget = Budget.objects.filter(userin=request.user).aggregate(total=Sum('budget'))
    totalexpense = Expense.objects.filter(expenser=request.user).aggregate(total=Sum('expense'))
    if  totalbudget['total'] is None or totalexpense['total'] is None:
        return render(request,'expense/detail.html',{'hey':w,'bud':i})
    elif totalbudget['total']-totalexpense['total'] < 100   :
        messages.error(request, "Your total expense is higher than the allocated budgets." )
        messages.info(request, "Kindly manage your expenses accordingly in these categories [food/automobile/water supply/electricity/entertainment/others]" )
        return render(request,'expense/detail.html',{'hey':w,'bud':i})
    else:
        return render(request,'expense/detail.html',{'hey':w,'bud':i})
@login_required()
def analysis(request):
        w = Expense.objects.filter(expenser=request.user).order_by('-dot')
        totalexpense = Expense.objects.filter(expenser=request.user).aggregate(total=Sum('expense'))
        i = Budget.objects.filter(userin=request.user)
        totalbudget = Budget.objects.filter(userin=request.user).aggregate(total=Sum('budget'))
        expenselabels = []
        expensedatas = []
        budgetlabels = []
        budgetdatas = []
        budgetqueryset = Budget.objects.filter(userin = request.user).order_by('dot')
        expensequeryset = Expense.objects.filter(expenser = request.user).order_by('dot')
        for expensevalue in expensequeryset:
            expenselabels.append(expensevalue.dot_pretty())
            expensedatas.append(expensevalue.expense)
        for budgetvalue in budgetqueryset:
            budgetlabels.append(budgetvalue.dot_pretty())
            budgetdatas.append(budgetvalue.budget)
        if totalbudget['total'] is None:
            messages.info(request, "*Get Started by adding Budget*" )
            return redirect('budget')
        elif totalexpense['total'] is None:
            messages.info(request, "*Enter Expense to continue.*" )
            return redirect('expense')
        else:
            if totalexpense['total']>totalbudget['total']:
                messages.error(request, "*Not enough Funds. Add Budget to Continue. Remember Your initial expense value will be deducted from the new Budget amount. Your Account is locked until that" )
                return redirect('budget')
            else:
                return render(request,'expense/analysis.html',{'hey':w,'bud':i,'totalexpense':totalexpense,'totalbudget':totalbudget,'expenselabels':expenselabels,'expensedatas':expensedatas,'budgetlabels':budgetlabels,'budgetdatas':budgetdatas})
def about(request):
    return render(request,'expense/about.html')
@login_required()
def report(request):
    response = HttpResponse(content_type = 'text/csv')
    writer = csv.writer(response)
    if request.GET.get('repo') == 'Expense':
        writer.writerow(['Title','Category','Expense','Date',' Mode of Payment '])
        for i in Expense.objects.filter(expenser = request.user).extra(select={'date':'dot'}).values_list('title','category','expense','date','payment'):
            writer.writerow(i)
        response['Content-Disposition'] = 'attachment;filename = "Expense_reports.csv"'
        return response
    else:
        writer.writerow(['Budget','Source','Category','Last Updated'])
        for i in Budget.objects.filter(userin= request.user).extra(select={'date':'dot'}).values_list('budget','source','category','date'):
                writer.writerow(i)
        response['Content-Disposition'] = 'attachment;filename = "Budget_reports.csv"'
        return response
@login_required()
def expensecharters(request):
    expenselinelabels = []
    expenselinedatas = []
    expenselabels = []
    expensedatas = []
    expensequeryset = Expense.objects.filter(expenser=request.user).order_by('-expense')
    automobileexpense = Expense.objects.filter(expenser = request.user,category = 'Automobile').aggregate(total = Sum('expense'))
    foodexpense = Expense.objects.filter(expenser = request.user,category = 'Food').aggregate(total = Sum('expense'))
    groceryexpense = Expense.objects.filter(expenser = request.user,category = 'Groceries').aggregate(total = Sum('expense'))
    electricityexpense = Expense.objects.filter(expenser = request.user,category = 'Electricity').aggregate(total = Sum('expense'))
    watersupplyexpense = Expense.objects.filter(expenser = request.user,category = 'Water Supply').aggregate(total = Sum('expense'))
    entertainmentexpense = Expense.objects.filter(expenser = request.user,category = 'Entertainment').aggregate(total = Sum('expense'))
    otherexpense = Expense.objects.filter(expenser = request.user,category = 'Others').aggregate(total = Sum('expense'))
    expenselinequeryset = Expense.objects.filter(expenser=request.user).order_by('dot')
    if automobileexpense['total'] is None:
        automobileexpense['total']  = 0
    if watersupplyexpense['total'] is None:
        watersupplyexpense['total'] = 0
    if foodexpense['total'] is None:
        foodexpense['total'] = 0
    if groceryexpense['total'] is None:
        groceryexpense['total'] = 0
    if electricityexpense['total'] is None:
        electricityexpense['total'] = 0
    if entertainmentexpense['total'] is None:
        entertainmentexpense['total'] = 0
    if otherexpense['total'] is None:
        otherexpense['total'] = 0
    expensedatastemp = {'Automobile':automobileexpense['total'],'Food':foodexpense['total'],'Groceries':groceryexpense['total'],'Entertainment':entertainmentexpense['total'],'Electricity':electricityexpense['total'],'Water Supply':watersupplyexpense['total'],'Others':otherexpense['total']}
    for i in expensedatastemp.keys():
        if not i in expenselabels:
            if expensedatastemp[i] !=0 :
                expenselabels.append(i)
                expensedatas.append(expensedatastemp[i])
    for expensevalue in expenselinequeryset:
        expenselinelabels.append(expensevalue.dot_pretty())
        expenselinedatas.append(expensevalue.expense)
    return render(request, 'expense/expensecharter.html', {'linelabels':expenselinelabels,'linedatas':expenselinedatas,'expenselabels':expenselabels,'expensedatas':expensedatas})
@login_required()
def budgetcharters(request):
    budgetlabels = []
    budgetdatas = []
    budgetlinelabels = []
    budgetlinedatas = []
    budgetqueryset = Budget.objects.filter(userin=request.user).order_by('dot')
    budgetlinequeryset = Budget.objects.filter(userin=request.user).order_by('dot')
    automobilebudget = Budget.objects.filter(userin = request.user,category = 'Automobile').aggregate(total = Sum('budget'))
    grocerybudget = Budget.objects.filter(userin = request.user,category = 'Groceries').aggregate(total = Sum('budget'))
    foodbudget = Budget.objects.filter(userin = request.user,category = 'Food').aggregate(total = Sum('budget'))
    electricitybudget = Budget.objects.filter(userin = request.user,category = 'Electricity').aggregate(total = Sum('budget'))
    watersupplybudget = Budget.objects.filter(userin = request.user,category = 'Water Supply').aggregate(total = Sum('budget'))
    entertainmentbudget = Budget.objects.filter(userin= request.user,category = 'Entertainment').aggregate(total = Sum('budget'))
    otherbudget= Budget.objects.filter(userin = request.user,category = 'Others').aggregate(total = Sum('budget'))
    if automobilebudget['total'] is None:
        automobilebudget['total']  = 0
    if watersupplybudget['total'] is None:
        watersupplybudget['total'] = 0
    if foodbudget['total'] is None:
        foodbudget['total'] = 0
    if electricitybudget['total'] is None:
        electricitybudget['total'] = 0
    if entertainmentbudget['total'] is None:
        entertainmentbudget['total'] = 0
    if grocerybudget['total'] is None:
        grocerybudget['total'] = 0
    if otherbudget['total'] is None:
        otherbudget['total'] = 0
    budgetdatastemp = {'Automobile':automobilebudget['total'],'Food':foodbudget['total'],'Groceries':grocerybudget['total'],'Entertainment':entertainmentbudget['total'],'Electricity':electricitybudget['total'],'Water Supply':watersupplybudget['total'],'Others':otherbudget['total']}
    for i in budgetdatastemp.keys():
        if not i in budgetlabels:
            if budgetdatastemp[i] !=0 :
                budgetlabels.append(i)
                budgetdatas.append(budgetdatastemp[i])
    for budgetvalue in budgetqueryset:
        budgetlinelabels.append(budgetvalue.dot_pretty())
        budgetlinedatas.append(budgetvalue.budget)
    return render(request, 'expense/budgetcharter.html', {'budgetlabels': budgetlabels,'budgetdatas': budgetdatas,'linelabels':budgetlinelabels,'linedatas':budgetlinedatas})
