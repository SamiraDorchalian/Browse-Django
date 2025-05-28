from django.shortcuts import render
from django.http import HttpRequest
from decimal import Decimal
from django.db.models import Q, F, Count, Min, Max, Sum, Avg
# from django.db.models.aggregates import Count

from .models import Product, Customer, OrderItem, Order, Comment

def show_data(request):
#       queryset = OrderItem.objects.filter(product_id=1)
#       queryset = Product.objects.filter(inventory=5)
#       queryset = Product.objects.filter(name__icontains='site', inventory__gt=3, inventory__lt=10)
#       queryset = Order.objects.filter(status=Order.ORDER_STATUS_UNPAID)
#       queryset = Order.objects.filter().exclude(status=Order.ORDER_STATUS_UNPAID)
#       queryset = OrderItem.objects.filter(order__id=1).exclude(quantity__gt=10)
#       queryset = Product.objects.filter(unit_price__lt=Decimal('10.0'))
#       queryset_david = Customer.objects.filter(first_name__icontains='david')
#       queryset = Order.objects.filter(customer__in=queryset_david)
#       queryset = Product.objects.filter(Q(inventory__lt=5) | Q(inventory__gt=95))
#       queryset = Product.objects.filter(~Q(inventory__lt=5) | Q(name__startswith='S'))
#       queryset = OrderItem.objects.filter(product__id=F('quantity'))
#       queryset = Product.objects.all()[:10]
#       queryset = Product.objects.all()[10:15]
#       queryset = Product.objects.order_by('unit_price')
#       queryset = Product.objects.filter(inventory__gt=90).order_by('-unit_price')
#       queryset = Product.objects.filter(inventory__gt=90).order_by('-unit_price').reverse()
#       queryset = Product.objects.filter(inventory__gt=90).order_by('-unit_price')[0]
#       queryset = Product.objects.filter(inventory__gt=90).order_by('unit_price')[0]
#       queryset = Product.objects.filter(inventory__gt=90).earliest('-unit_price')
      # queryset = Product.objects.filter(inventory__gt=90).latest('-unit_price')
      # queryset = Product.objects.values('id', 'name', 'unit_price')
      # queryset = Product.objects.order_by('-inventory').values('name', 'inventory')
      # queryset = OrderItem.objects.values('product_id').distinct()
      # queryset_orderitems_products = OrderItem.objects.values('product_id').distinct()
      # queryset = Product.objects.filter(id__in=queryset_orderitems_products)
      # queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct())
      # queryset = OrderItem.objects.values_list('id', 'product_id')
      # queryset = Product.objects.only('id', 'name', 'inventory') # چه چیز های رو فقط میخام
      # queryset = Product.objects.values('id', 'name') 
      # queryset = Product.objects.defer('unit_price') # چه چیز هایی رو نمیخام
      # queryset = OrderItem.objects.select_related('product').all() # مربوط به فیلدی که ForeignKey خورده .
      # queryset = Product.objects.prefetch_related('order_items').all()  # برعکس بالایی عمل میکنه مثلا متد پروداکت در فایل مدل در کدوم اوردرایتم ها استفاده شده 
      # queryset = Comment.objects.select_related('product').all()
      # queryset = Product.objects.prefetch_related('comments').all()
      # queryset = Product.objects.select_related('category').prefetch_related('comments').all()
      # queryset = Order.objects.prefetch_related('items__product').select_related('customer').all()
      # queryset = Product.objects.aggregate(Count('id'))
      # queryset = Comment.objects.aggregate(Count('id'))
      # queryset = OrderItem.objects.aggregate(Count('id'))
      # queryset = Product.objects.aggregate(avg=Avg('unit_price'))
      # queryset = Product.objects.aggregate(count=Count('id'), avg=Avg('unit_price'))
      # queryset = Product.objects.aggregate(
      #       count=Count('id'), 
      #       avg=Avg('unit_price'), 
      #       max_inv=Max('inventory'),
      # )
      # queryset = Product.objects.filter(inventory__gt=10).aggregate(
      #       count=Count('id'),
      #       price_avg=Avg('unit_price'),
      # )
      # queryset = OrderItem.objects.filter(product_id=2).aggregate(Count('id'))
      # product = Product.objects.get(id=1)
      # print(product.order_items.aggregate(count=Count('id')))
      queryset = OrderItem.objects.values('product_id').distinct()
      print(queryset.count())
      return render(request, 'hello.html' )
      # print(list(queryset))
#       print([x.unit_price for x in list(queryset)])
      # print(len(list(queryset)))
      # list(queryset)
      # return render(request, 'hello.html', {'order_items': list(queryset) } )
#     return render(request, 'hello.html', {'customers': list(queryset)})
