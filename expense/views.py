from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request,'expense/home.html')
def add(request):
    return render(request,'expense/add.html')
