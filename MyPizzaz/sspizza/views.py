from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from .models import *

def home(request):
    pizzas = Pizza.objects.all()
    context = {'pizzas': pizzas}
    return render(request, 'sspizza/dashboard.html', context)
    # return HttpResponse('Welcome to the development of She Said Pizza')