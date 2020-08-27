from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=100)
    address = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class VegTopping(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class NonVegTopping(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.FloatField(null=True)
    
    def __str__(self):
        return self.name


class Base(models.Model):
    SIZE = (
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
        ('Xlarge', 'Xlarge')
    )
    crustName = models.CharField(max_length=100)
    size = models.CharField(max_length=10, default='Medium', choices=SIZE)
    price = models.FloatField(null=True)

    def __str__(self):
        return self.crustName

class Order(models.Model):
    STATUS = (
        ('Pending', 'Pending'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered')
    )
    customer = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)

    pizza = models.ForeignKey(Pizza, null=True, on_delete=models.SET_NULL)
    vegToppings = models.ManyToManyField(VegTopping)
    nonVegToppings = models.ManyToManyField(NonVegTopping)
    baseCrust = models.ForeignKey(Base, null=True, on_delete=models.SET_NULL)

    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=200, null=True, choices=STATUS)

    def __str__(self):
        return self.pizza.name