from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class Expense(models.Model):
    title=models.CharField(max_length=100)
    expense=models.PositiveIntegerField(validators = [MinValueValidator(0)])
    dot=models.DateField(auto_now_add = True)
    Category_Choices = [
        ('Food','Food'),
        ('Automobile','Automobile'),
        ('Electricity','Electricity'),
        ('Water Supply','Water Supply'),
        ('Entertainment','Entertainment'),
        ('Others','Others'),

    ]
    category=models.CharField(max_length=150,choices = Category_Choices, default = 'Food' )
    expenser=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    receipt=models.ImageField(upload_to='images/', blank = True)
    Payment_Choices = [
        ('Cash','Cash'),
        ('Credit Card','Credit Card'),
        ('Debit Card','Debit Card'),
        ('Other Source','Other Source'),
    ]
    payment=models.CharField(max_length=100,choices = Payment_Choices,default='Cash')
    def dot_pretty(self):
        return self.dot.strftime('%b   %e   %Y')
    def __str__(self):
        return self.title
class Budget(models.Model):
    budget=models.PositiveIntegerField(validators = [MinValueValidator(0)])
    dot=models.DateField(auto_now_add = True)
    Source_Choices = [
        ('Salary','Salary'),
        ('Bank','Bank'),
        ('Other Source','Other Source'),
    ]
    Budget_Category_Choices = [
        ('Food','Food'),
        ('Automobile','Automobile'),
        ('Electricity','Electricity'),
        ('Water Supply','Water Supply'),
        ('Entertainment','Entertainment'),
        ('Others','Others'),
    ]
    category = models.CharField(max_length = 100,choices = Budget_Category_Choices)
    source=models.CharField(max_length=50, choices = Source_Choices)
    userin=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    def dot_pretty(self):
        return self.dot.strftime('%b   %e   %Y')
