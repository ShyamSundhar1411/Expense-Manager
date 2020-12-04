import django_filters
from django_filters import ChoiceFilter
from .models import Expense,Budget
class ExpenseFilter(django_filters.FilterSet):
    order = [
        ('ascending','Ascending'),
        ('descending','Descending'),
    ]
    ordering = ChoiceFilter(label = 'Date ordering',choices = order , method = 'filter_by_order')
    highexpense = ChoiceFilter(label = 'Expense Ordering',choices = order,method = 'filter_by_expense')
    class Meta:
        model = Expense
        fields = ['title','category','payment']

    def filter_by_order(self,queryset,name,value):
        expression = 'dot' if value == 'ascending' else '-dot'
        return queryset.order_by(expression)
    def filter_by_expense(self,queryset,name,value):
        expression = 'expense' if value == 'ascending' else '-expense'
        return queryset.order_by(expression)
class BudgetFilter(django_filters.FilterSet):
    order = [
        ('ascending','Ascending'),
        ('descending','Descending'),
    ]
    ordering = ChoiceFilter(label = 'Date Ordering',choices = order, method = 'filter_by_order')
    highbudget = ChoiceFilter(label = 'Budget Ordering', choices = order, method = 'filter_by_budget')
    class Meta:
        model = Budget
        fields = ['source','category']
    def filter_by_order(self,queryset,name,value):
        expression = 'dot' if value == 'ascending' else '-dot'
        return queryset.order_by(expression)
    def filter_by_budget(self,queryset,name,value):
        expression = 'budget' if value == 'ascending' else '-budget'
        return queryset.order_by(expression)
