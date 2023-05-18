from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.views import View
# Create your views here.


def home(request):
    if request.user.is_authenticated:
        return render(request, 'home.html', {'Title': 'home',})
    else:
        return redirect('login')


def add(request):
    num1 = float(request.POST['num1'])
    num2 = float(request.POST['num2'])
    return render(request, 'add.html', {'sum': num1+num2})


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        conformpassword = request.POST['conformpassword']
        if password == conformpassword:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
                return redirect('signin')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'username already exists')
                return redirect('signin')
            else:
                new_user = User.objects.create_user(username, email, password)
                new_user.save()
                messages.info(request, 'your account created successfully\n log in now')
                return redirect('login')
        else:
            messages.info(request, 'password is not matching')
            return redirect('signin')
    else:
        return render(request, 'signin.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'email or password does not match')
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


@login_required
def deletion(request):
    user = request.user
    if request.method == 'POST':
        # conformation = request.POST.get('conformation')
        # if conformation == 'yes':
        #     return HttpResponse('<h1>hello world</h1>')
            if 'yes' in request.POST.get('conformation'):
                user.delete()
                auth.logout(request)
                return HttpResponse('<h1>account deleted successfully</h1>')
            elif 'no' in request.POST.get('conformation'):
                return redirect('home')
    return render(request, 'account-delete.html')


@login_required
def update(request):
    return render(request, 'signin.html')
