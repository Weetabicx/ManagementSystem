from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import User

from datetime import datetime, timedelta

def user_login(request):

  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username, password=password)
    if user:
      login(request,user)
      return redirect('rota')
    form = LoginForm(request.POST)
    return render(request, 'login.html', {'form': form})

  else:
    form = LoginForm(request.POST)
    return render(request, 'login.html', {'form': form})

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def availability(request):
    if request.method == "POST":
      avail = request.POST.getlist('availability')
      user = request.user
      user.availability  = avail
      user.save()
      return redirect('rota')
      
    today = datetime.now().weekday()
    monday = datetime.now() - timedelta(days=today)

    days = {}
    for i in range(0, 7):
      days[i] = (monday + timedelta(days=i)).strftime('%A %d/%m/%Y')


    return render(request, 'availability.html',
                  {'days': days.values(),
                  'weekdays': range(0,7)})

@login_required
def rota(request):
    today = datetime.now().weekday()
    monday = datetime.now() - timedelta(days=today)

    days = {}
    for i in range(0, 7):
      days[i] = (monday + timedelta(days=i)).strftime('%A %d/%m/%Y')


    return render(request, 'rota.html',
                  {'days': days.values(),
                  'weekdays': range(0,7)})