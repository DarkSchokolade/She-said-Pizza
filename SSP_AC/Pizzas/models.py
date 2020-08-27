from django.db import models

# Create your models here.
class Food_type(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Ingredients(models.Model):
    Ingredient = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.Ingredient

class Chef_Pizzas(models.Model):
    name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    ingredient = models.ManyToManyField(Ingredients)
    price = models.FloatField(null=True)
    food_type = models.ManyToManyField(Food_type)

    def __str__(self):
        return self.name
        # Returns name of the pizza