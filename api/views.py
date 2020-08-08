#Rest Framework
from rest_framework import generics, permissions
from rest_framework.authtoken.models import Token
from rest_framework.parsers import JSONParser
#Django Framework
from django.shortcuts import render
from expense.models import Expense,Budget
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.db import IntegrityError
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
#Serializers
from .serializers import ExpenseAddSerialzer,BudgetAddSerialzer
#Class Based Views
class AddExpense(generics.ListCreateAPIView):
    serializer_class = ExpenseAddSerialzer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Expense.objects.filter(expenser = user).order_by('-dot')
    def perform_create(self,serializer):
        serializer.save(expenser = self.request.user)

class UpdateDestroyExpense(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ExpenseAddSerialzer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Expense.objects.filter(expenser = user)
class AddBudget(generics.ListCreateAPIView):
    serializer_class = BudgetAddSerialzer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Budget.objects.filter(userin=user).order_by('-dot')
    def perform_create(self,serializer):
        serializer.save(userin = self.request.user)
class UpdateDestroyBudget(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BudgetAddSerialzer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Budget.objects.filter(userin = user)
#Function Based Views
'''@csrf_exempt
def signup(request):
    if request.method == 'POST':
        try:
            data = JSONParser().parse(request)
            user = User.objects.create_user(data['username'], password = data['password'])
            user.save()
            token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)}, status = 201)
        except IntegrityError:
            return JsonResponse({'error':'That username has already been taken. Please choose a new username'},status = 400)

@csrf_exempt
def login(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        user = authenticate(request,username = data["username"],password = data['password'])
        if user is None:
            return JsonResponse({'error':'Could not login. Please check username and password'},status = 400)
        else:
            try:
                token = Token.objects.get(user=user)
            except:
                token = Token.objects.create(user=user)
            return JsonResponse({'token':str(token)},status = 200)
'''
