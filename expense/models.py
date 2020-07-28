from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
    title=models.CharField(max_length=100)
    expense=models.IntegerField(default=0)
    category=models.CharField(max_length=150)
    dot=models.DateTimeField()
    expenser=models.ForeignKey(User,on_delete = models.CASCADE)
    receipt=models.ImageField(upload_to='images/', blank = True)
    payment=models.CharField(max_length=100,default='cash')
    def dot_pretty(self):
        return self.dot.strftime('%b %e %Y')
    def dot_pretty(self):
        return self.dot.strftime('%b %e %Y')
    def dot_w(self):
        return self.dot.strftime('%W')
    def dot_y(self):
        return self.dot.strftime('%Y')
    def dot_m(self):
        return self.dot.strftime('%m')
    def __str__(self):
        return self.title
class Budget(models.Model):
    budget=models.PositiveIntegerField(default=0)
    dot=models.DateTimeField()
    source=models.CharField(max_length=50,default='Salary Income')
    userin=models.ForeignKey(User,on_delete = models.CASCADE)
    def dot_pretty(self):
        return self.dot.strftime('%b %e %Y')
