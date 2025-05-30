from django.contrib import admin
from django.db.models import Count

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
    

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'status', ]
    list_editable = ['status']
    list_per_page = 10


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # list_display =['id', 'customer', 'status', 'datetime_create', ]
    list_display =['id', 'customer', 'status', 'datetime_create', 'num_of_items',]
    list_editable = ['status']
    list_per_page = 10
    ordering = ['-datetime_create']

    # prefetch related and change query in Admin / Make a new query

    def get_queryset(self, request):
        return super() \
        .get_queryset(request) \
        .prefetch_related('items') \
        .annotate(
            items_count=Count('items')
        )

    @admin.display(ordering='items_count')
    def num_of_items(self, order): # by related_name='orders' in file models / ForeignKey
        # return order.items.count()
        return order.items_count


# admin.site.register(Product, ProductAdmin)
admin.site.register(Category)