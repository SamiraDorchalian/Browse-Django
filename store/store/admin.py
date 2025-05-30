from django.contrib import admin

from .models import Category, Order, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'inventory', 'unit_price', 'datetime_create',]
    list_per_page = 10
    list_editable = ['unit_price']
    ordering = ['-datetime_create']

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display =['id', 'customer', 'status', 'datetime_create', ]
    list_editable = ['status']
    list_per_page = 10
    ordering = ['-datetime_create']

# admin.site.register(Product, ProductAdmin)
admin.site.register(Category)