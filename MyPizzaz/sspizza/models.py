from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# instead of having a separate customerInfo just put the info in order [simple is better]
class Crust(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.FloatField(null=True)

    def __str__(self):
        return self.name

class Topping(models.Model):
    # CAT_F is veg or nonveg
    CAT_F = (
        ('VEG', 'VEG'),
        ('NON-VEG', 'NON-VEG')
    )
    name = models.CharField(max_length=200, null=True)
    category = models.CharField(max_length=10, choices=CAT_F)
    price = models.FloatField(null=True)

    def __str__(self):
        return self.name

class Pizza(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    crust =  models.ForeignKey(Crust, null=True, on_delete=models.SET_NULL)
    topping = models.ManyToManyField(Topping)

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    
    def __str__(self):
        return self.name


class OrderCart(models.Model):
    # customer = models.ForeignKey(CustomerInfo, null=True, on_delete=models.SET_NULL)
    # user =  models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    # phone = models.CharField(max_length=100)
    # address = models.TextField()

    pizza = models.ForeignKey(Pizza, null=True, on_delete=models.SET_NULL)
    date_created = models.DateTimeField(auto_now_add=True)
    total_price = models.FloatField(null=True)
    
    def __str__(self):
        return self.pizza.name