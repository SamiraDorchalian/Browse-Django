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
      queryset = Product.objects.filter(inventory__gt=90).latest('-unit_price')


#       print([x.unit_price for x in list(queryset)])
#       list(queryset)
      return render(request, 'hello.html', )
#     return render(request, 'hello.html', {'customers': list(queryset)})
