#Rest Framework
from rest_framework import serializers
from expense.models import Expense,Budget

#Serializers
class ExpenseAddSerialzer(serializers.ModelSerializer):
    dot = serializers.ReadOnlyField()
    class Meta:
        model = Expense
        fields = ('id','title','expense','category','payment','receipt','dot')
class BudgetAddSerialzer(serializers.ModelSerializer):
    dot = serializers.ReadOnlyField()
    class Meta:
        model = Budget
        fields = ['id','budget','source','dot']
