from django.shortcuts import render, redirect,render_to_response
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login


# Create your views here.

def home(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request,"home.html",{})

def about(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request,"about.html",{})

def gallery(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request,"gallery.html",{})

def login(request, *args, **kwargs):
    print(args, kwargs)
    print(request.user)
    return render(request,"login.html",{})

def signup (request , *args, **kwargs):
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return render(request,'home.html',{})

    else:
        form=UserCreationForm()
    return render(request,"registration/register.html",{'form':form})



