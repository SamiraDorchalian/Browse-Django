from django.contrib import admin, messages
from django.db.models import Count
from django.utils.html import format_html
from django.urls import reverse
from django.utils.http import urlencode

from .models import Category, Customer, Order, Product ,Comment

# Custom Filtering
class InventoryFilter(admin.SimpleListFilter):
    LESS_THAN = '<3'
    BETWEEN_3_AND_10 = '3<=10'
    MORE_THAN_10 = '>10'

    title = 'Critical Inventory Status'
    parameter_name = 'inventory'

    def lookups(self, request, model_admin):
        return [
            (InventoryFilter.LESS_THAN, 'High'),
            (InventoryFilter.BETWEEN_3_AND_10, 'Medium'),
            (InventoryFilter.MORE_THAN_10, 'OK'),
        ]
    
    def queryset(self, request, queryset):
        if self.value() == InventoryFilter.LESS_THAN:
            return queryset.filter(inventory__lt=3)
        if self.value() == InventoryFilter.BETWEEN_3_AND_10:
            # return queryset.filter(inventory__lt=10, inventory__gt=3)
            return queryset.filter(inventory__range=(3, 10))
        if self.value() == InventoryFilter.MORE_THAN_10:
            return queryset.filter(inventory__lt=10)
        # return super().queryset(request, queryset)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # list_display = ['id', 'name', 'inventory', 'unit_price', 'is_low', ]
    list_display = ['id', 'name', 'inventory', 'unit_price', 'inventory_status', 'product_category' ,'num_of_comments' ]
    list_per_page = 10
    list_editable = ['unit_price']
    # ordering = ['-datetime_create']
    list_select_related = ['category']
# Custom Filtering
    list_filter = ['datetime_create', InventoryFilter]
# Custom action
    actions = ['clear_inventory']
# Prepopulated Fields
    prepopulated_fields = {
        'slug': ['name', ]
    }

    def get_queryset(self, request):
        return super().get_queryset(request) \
                .prefetch_related('comments') \
                .annotate(
                    comments_count=Count('comments'),
                )


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
    
    @admin.display(description='# comments', ordering='comments_count')
    def num_of_comments(self, product):
        # return product.comments_count
# add link to panelAdmin 
# این لینک تمام کامنت های مربوط به اون محصول رو نشون میده
        url = (
            reverse('admin:store_comment_changelist')
            + '?'
            + urlencode({
                'product__id': product.id,
            })
        )
        return format_html('<a href="{}">{}</a>', url, product.comments_count)

    
# select related in ListAdmin
    # @admin.display(ordering='category_id') # for sort default in panel admin
    @admin.display(ordering='category__title') # for sort default in panel admin
    def product_category(self, product):
        return product.category.title
    
# Custom action    
    @admin.action(description='Clear inventory')
    def clear_inventory(self, request, queryset):
        # queryset.update(inventory=0)
        update_count = queryset.update(inventory=0)
        self.message_user(
            request,
            f'{update_count} of product inventories cleared to zero.',
            # messages.ERROR,
            messages.SUCCESS,
            # messages.WARNING,
        )
        
        

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'status', ]
    list_editable = ['status']
    list_per_page = 10
    # list_display_links = ['id', 'product'] # for change link



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
# description for change name
    @admin.display(ordering='items_count', description='# items')
    def num_of_items(self, order): # by related_name='orders' in file models / ForeignKey
        # return order.items.count()
        return order.items_count


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email',]
    list_per_page = 10
    ordering = ['last_name', 'first_name', ]
# Search Fields / add Search box in panelAdmin
    # search_fields = ['first_name', 'last_name', ]
    # search_fields = ['first_name__startswith', 'last_name__startswith', ] # What word should it start with? & Case sensitive
    search_fields = ['first_name__istartswith', 'last_name__istartswith', ] # its not Case sensitive => istartswith


# admin.site.register(Product, ProductAdmin)
admin.site.register(Category)