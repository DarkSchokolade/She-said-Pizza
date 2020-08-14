from django.urls import path
from . import views

app_name = 'sspizza'
urlpatterns = [
    path('', views.home, name='home'),
]