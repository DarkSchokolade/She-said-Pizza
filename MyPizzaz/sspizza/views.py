from django.shortcuts import render, redirect
from django.http import HttpResponse

from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
# Create your views here.
from .models import *
from .forms import * 


def home(request):
    menu = Menu.objects.all()
    context = {'menu': menu}
    return render(request, 'sspizza/dashboard.html', context)

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

def LogoutUser(request):
    logout(request)
    return redirect('sspizza:home')

def CreateOrder(request):
    form = OrderForm()
    context = {'form':form}
    return render(request, 'sspizza/create_order.html', context)

def PlaceOrder(request, pk):

    form = OrderForm()
    context = {'form':form}

    if request.method == 'POST':
        print('Printing POST:', request.POST)
        form = OrderForm(request.POST)
        delivery_form = DeliveryInfo()
        
        if form.is_valid():
            pizza = form.save(commit=False)
            pizza.created_by = request.user
            pizza.save()
            # so this gets the topping "id" from the POST request 
            topping_info = request.POST.getlist('topping')
            print(topping_info)
            # then loop over the toppings list and then add them to pizza,
            # because pizza should save first and then add the manytomany relation (ref: Docs->ManyToMany)
            total_topping_price = 0
            for topping_num in topping_info:
                pizza.topping.add(topping_num)
                topping_price = Topping.objects.get(id=topping_num).price
                total_topping_price += topping_price
                print(topping_price)

            print('Total topping price: ', total_topping_price)   # logic of calculation works
            total_amount = total_topping_price + pizza.crust.price

            bill = OrderCart(pizza=pizza, total_price=total_amount)
            bill.save()
        else:
            print(form._errors)
            print("shit ")
            return render(request, 'sspizza/create_order.html', context)

    context = {
        'pizza': pizza, 'total_topping_price': total_topping_price,
        'total_amount': total_amount, 'delivery_form': delivery_form
        }
    return render(request, 'sspizza/place_order.html', context)

def GenerateBill(request, pk):
    if request.method == 'POST':
        order = OrderCart.objects.get(pizza=pk)

        contact_name = request.POST.get('contact_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
      
        order.contact_name = contact_name
        order.phone = phone
        order.address = address
        order.save()
    context = {'order': order}
    return render(request, 'sspizza/bill.html',context)

# for menu items
def OrderMenu(request, p_key):
    delivery_form = DeliveryInfo()
    menu_item = Menu.objects.get(id=p_key)
    print(menu_item)
    if request.method == 'POST':
        delivery_form = DeliveryInfo(request.POST)
        if delivery_form.is_valid():
            menu_order = delivery_form.save(commit=False)
            menu_order.menu = menu_item
            menu_order.total_price = menu_item.price
            menu_order.save()
            print(menu_order.id)
            return redirect('sspizza:menu_bill', p_key=menu_order.id)
    context = {'menu_item': menu_item,'delivery_form': delivery_form}
    return render(request, 'sspizza/menu_order.html', context)

def MenuBill(request, p_key):
    order = OrderCart.objects.get(id=p_key)
    context = {'order': order}
    return render(request, 'sspizza/bill.html',context)
