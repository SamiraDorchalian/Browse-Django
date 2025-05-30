from django.contrib import admin

from .models import Category, Order, Product

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name', 'inventory', 'unit_price', 'is_low', ]
    list_display = ['id', 'name', 'inventory', 'unit_price', 'inventory_status', ]
    list_per_page = 10
    list_editable = ['unit_price']
    # ordering = ['-datetime_create']

    # Computed Fields

    # def is_low(self, product):
    #     return product.inventory < 10
    
    # def inventory_status(self, product):
    def inventory_status(self, product: Product):
        if product.inventory < 10:
            return 'Low'
        if product.inventory > 50:
            return 'High'
        return 'Medium'


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display =['id', 'customer', 'status', 'datetime_create', ]
    list_editable = ['status']
    list_per_page = 10
    ordering = ['-datetime_create']

# admin.site.register(Product, ProductAdmin)
admin.site.register(Category)