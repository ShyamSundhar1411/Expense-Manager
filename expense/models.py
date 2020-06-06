from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
    title=models.CharField(max_length=100)
    expense=models.IntegerField(default=0)
    category=models.CharField(max_length=150)
    dot=models.DateTimeField()
    budget=models.PositiveIntegerField(default=0)
    expenser=models.ForeignKey(User,on_delete = models.CASCADE)
    transactions=models.IntegerField(default=0)
    def budget_left(self):
        if self.expense!=0:
            return self.budget-self.expense
        else:
            return self.budget
    def dot_pretty(self):
        return self.dot.strftime('%b %e %Y')
    def __str__(self):
        return self.title
    def all(self,n):
        return self.budget+n
