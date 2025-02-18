from django.contrib import admin
from store.models import Order, Product



admin.site.register(Product)
admin.site.register(Order)