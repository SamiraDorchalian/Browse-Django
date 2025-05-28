from django.shortcuts import render
from django.http import HttpRequest
from decimal import Decimal
from django.db.models import Q, F

from .models import Product, Customer, OrderItem, Order

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
      queryset = Product.objects.prefetch_related('order_items').all()

#       print([x.unit_price for x in list(queryset)])
      print(list(queryset))
      # print(len(list(queryset)))
      # list(queryset)
      # return render(request, 'hello.html', {'order_items': list(queryset) } )
      return render(request, 'hello.html', {'products': list(queryset) } )
#     return render(request, 'hello.html', {'customers': list(queryset)})
