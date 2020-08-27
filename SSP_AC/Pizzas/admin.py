from django.contrib import admin

# Register your models here.
from .models import * 

admin.site.register(Food_type)
admin.site.register(Chef_Pizzas)
admin.site.register(Ingredients)