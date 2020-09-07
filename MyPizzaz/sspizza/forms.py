from django.forms import ModelForm
from django import forms

from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from .models import Pizza, OrderCart

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class OrderForm(ModelForm):
    class Meta:
        model = Pizza
        fields = '__all__'
        exclude = ['created_by']

class DeliveryInfo(ModelForm):
    class Meta:
        model = OrderCart
        fields = ['contact_name', 'phone', 'address']