from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Expense(models.Model):
    title=models.CharField(max_length=100)
    expense=models.IntegerField(default=0)
    category=models.CharField(max_length=150)
    dot=models.DateTimeField()
    expenser=models.ForeignKey(User,on_delete = models.CASCADE)
    transactions=models.IntegerField(default=0)
    receipt=models.ImageField(upload_to='images/')
    def dot_pretty(self):
        return self.dot.strftime('%b %e %Y')
    def __str__(self):
        return self.title
class Budget(models.Model):
    budget=models.PositiveIntegerField(default=0)
    userin=models.ForeignKey(User,on_delete = models.CASCADE)
    dot=models.DateTimeField()
    def dot_pretty(self):
        return self.dot.strftime('%b %e %Y')
