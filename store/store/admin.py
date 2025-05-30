from django.contrib import admin

from .models import Category, Order, Product ,Comment

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name', 'inventory', 'unit_price', 'is_low', ]
    list_display = ['id', 'name', 'inventory', 'unit_price', 'inventory_status', 'product_category' ]
    list_per_page = 10
    list_editable = ['unit_price']
    # ordering = ['-datetime_create']
    list_select_related = ['category']

    # Computed Fields

    # def is_low(self, product):
    #     return product.inventory < 10
    
    # def inventory_status(self, product):
    def inventory_status(self, product: Product): #product: Product for suggestion by VSCode
        if product.inventory < 10:
            return 'Low'
        if product.inventory > 50:
            return 'High'
        return 'Medium'
    
    # select related in ListAdmin

    # @admin.display(ordering='category_id') # for sort default in panel admin
    @admin.display(ordering='category__title') # for sort default in panel admin
    def product_category(self, product):
        return product.category.title


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display =['id', 'customer', 'status', 'datetime_create', ]
    list_editable = ['status']
    list_per_page = 10
    ordering = ['-datetime_create']

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'status', ]
    list_editable = ['status']
    list_per_page = 10


# admin.site.register(Product, ProductAdmin)
admin.site.register(Category)