from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method=='POST':
        if request.POST['password1']==request.POST['password2'] and request.POST['Username'] !="" and len(request.POST['password1'])>=8:
            try:
                user=User.objects.get(username=request.POST['Username'])
                return render(request,'accounts/signup.html',{'error':'Username is already taken.Try different one'})
            except User.DoesNotExist:
                user=User.objects.create_user(username=request.POST['Username'],password=request.POST['password1'])
                auth.login(request,user)
                return render(request,'expense/budget.html',{'wel':'Enter Budget to continue to home page🙂'})
        elif request.POST['Username']=='':
            return render(request,'accounts/signup.html',{'error':'*All fields are required*'})
        elif len(request.POST['password1'])<8:
            return render(request,'accounts/signup.html',{'error':'*Password must be atleast 8 characters*'})
        else:
            return render(request,'accounts/signup.html',{'error':'*Passwords must match*'})
    else:
        return render(request,'accounts/signup.html')
def login(request):
    if request.method=='POST':
        user=auth.authenticate(username=request.POST['Username'],password=request.POST['password1'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            if request.POST['Username']=='' and request.POST['password1']=='':
                return render(request,'accounts/login.html',{'error':'*All fields are required*'})
            else:
                return render(request,'accounts/login.html',{'error':'*Username or password is wrong*'})
    else:
        return render(request,'accounts/login.html')
def logout(request):
    if request.method=='POST':
        auth.logout(request)
        return redirect('home')
