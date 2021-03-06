from django.urls import path
from . import views

app_name = 'sspizza'
urlpatterns = [
    path('register/', views.RegisterPage, name='register'),
    path('login/', views.LoginPage, name='login'),
    path('logout/', views.LogoutUser, name='logout'),
    
    path('', views.home, name='home'),
    path('create_order/', views.CreateOrder, name='create_order'),
    path('place_order/<str:pk>/', views.PlaceOrder, name='place_order'),
    path('bill/<str:pk>/', views.GenerateBill, name='bill'),

    path('order_menu/<str:p_key>/', views.OrderMenu, name='order_menu'),
    path('menu_bill/<str:p_key>/', views.MenuBill, name='menu_bill'),
]