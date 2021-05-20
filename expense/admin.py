from django.contrib import admin
from .models import Expense,Budget,Profile
# Register your models here.
admin.site.register(Expense)
admin.site.register(Budget)
admin.site.register(Profile)
