from django.shortcuts import render, redirect
from .models import Employee
from django.contrib.auth.models import User, auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages

def home(request):
    users = User.objects.all()
    return render(request, 'index.html', {'users': users})

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('/home')
        else:
            messages.info(request, 'Invalid credentials')
            return redirect('/')
    else:
        return render(request, 'login.html')

@csrf_exempt
def login_as(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = User.objects.get(username=username)
        users = User.objects.all()

        if request.user.is_superuser:
            if request.user.username == username:
                print('isti username')
                return render(request, 'index.html', {'users': users, 'alert_flag_1': True})
            else:
                auth.login(request, user)
                return render(request, 'index.html', {'users': users})
        else:
            return render(request, 'index.html', {'alert_flag': True, 'users': users})
    else:
        users = User.objects.all()
        return render(request, 'index.html', {'users': users})

def logout(request):
    auth.logout(request)
    return redirect('/')