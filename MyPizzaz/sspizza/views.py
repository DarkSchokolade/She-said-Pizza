from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, 'sspizza/dashboard.html')
    # return HttpResponse('Welcome to the development of She Said Pizza')