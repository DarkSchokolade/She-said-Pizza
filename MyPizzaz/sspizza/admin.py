from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register(Pizza)
admin.site.register(VegTopping)
admin.site.register(NonVegTopping)
admin.site.register(Base)
admin.site.register(Customer)
admin.site.register(Order)