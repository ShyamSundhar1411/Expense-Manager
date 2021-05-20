from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Expense, Budget, Profile

class UserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username","email","password1", "password2")
class BudgetCreationForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ('budget','category','source')
class ExpenseCreationForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('title','expense','category','receipt','payment')
