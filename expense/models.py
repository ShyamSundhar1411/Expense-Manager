from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.text import slugify
import uuid
from PIL import Image
# Create your models here.
class Expense(models.Model):
    title=models.CharField(max_length=100)
    expense=models.PositiveIntegerField(validators = [MinValueValidator(0)])
    dot=models.DateField(auto_now_add = True)
    Category_Choices = [
        ('Food','Food'),
        ('Automobile','Automobile'),
        ('Groceries','Groceries'),
        ('Electricity','Electricity'),
        ('Water Supply','Water Supply'),
        ('Entertainment','Entertainment'),
        ('Others','Others'),

    ]
    category=models.CharField(max_length=150,choices = Category_Choices, default = 'Food' )
    expenser=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    receipt=models.ImageField(upload_to='receipts/', blank = True)
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
        ('Groceries','Groceries'),
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
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete = models.CASCADE)
    avatar = models.ImageField(upload_to = 'avatar/',blank = True)
    bio = models.TextField(blank = True,max_length = 500)
    slug = models.SlugField(blank = True,max_length = 100)


    def __str__(self):
        return self.user.username
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = uuid.uuid4()
        super(Profile,self).save(*args,**kwargs)
@receiver(post_save,sender = User)
def create_profile(sender,instance,created,**kwargs):
    if created:
        Profile.objects.create(user = instance)
        instance.profile.save()
@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
