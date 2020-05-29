from django.db import models

# Create your models here.
class Expense(models.Model):
    title=models.CharField(max_length=100)
    expense=models.IntegerField()
    category=models.CharField(max_length=150)
    dot=models.DateTimeField()
    def dot_pretty(self):
        return self.dot.strftime('%b %e %Y')
    def __str__(self):
        return self.title
