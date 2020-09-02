from django.urls import path
from . import views

app_name = 'sspizza'
urlpatterns = [
    path('register/', views.RegisterPage, name='register'),
    path('login/', views.LoginPage, name='login'),
    path('', views.home, name='home'),
    path('create_order/', views.create_Order, name='create_order'),
    path('place_order/<str:pk>', views.PlaceOrder, name='place_order')
]