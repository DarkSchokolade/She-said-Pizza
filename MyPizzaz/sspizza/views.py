from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.
from .models import *
from .forms import * 
def home(request):
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    return render(request, 'sspizza/dashboard.html', context)
    # return HttpResponse('Welcome to the development of She Said Pizza')

def RegisterPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sspizza:login')
    context = {'form': form}
    return render(request, 'sspizza/register.html', context)

def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('sspizza:home')
        else:
            messages.info(request, 'Password or Username must be incorrect')
    return render(request, 'sspizza/login.html')

def create_Order(request):
    form = OrderForm()
    context = {'form':form}
    return render(request, 'sspizza/create_order.html', context)

def PlaceOrder(request, pk):

    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = OrderForm(request.POST)
        if form.is_valid():
            pizza = form.save(commit=False)
            pizza.created_by = request.user
            pizza.save()
        else:
            print(form._errors)

    context = {'pizza': pizza}
    return render(request, 'sspizza/place_order.html', context)