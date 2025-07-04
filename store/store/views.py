from decimal import Decimal
from django.db import transaction, connection
from django.db.models import Q, F, Count, Min, Max, Sum, Avg , Value, Func, ExpressionWrapper, DecimalField, Prefetch
from django.db.models.aggregates import Count
from django.http import HttpRequest
from django.shortcuts import render

from .models import Product, Customer, OrderItem, Order, Comment, Category


# @transaction.atomic()
def show_data(request):
      # objects = Manager
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
      
      # values & values_list & only & defer
      
      # queryset = Product.objects.values('id', 'name', 'unit_price')
      # queryset = Product.objects.order_by('-inventory').values('name', 'inventory')
      # queryset = OrderItem.objects.values('product_id').distinct() #ردیف‌های تکراری رو از نتایج کوئری حذف میکنه
      # queryset_orderitems_products = OrderItem.objects.values('product_id').distinct()
      # queryset = Product.objects.filter(id__in=queryset_orderitems_products)
      # queryset = Product.objects.filter(id__in=OrderItem.objects.values('product_id').distinct())
      # queryset = OrderItem.objects.values_list('id', 'product_id')
      # queryset = Product.objects.only('id', 'name', 'inventory') # چه چیز های رو فقط میخام
      # queryset = Product.objects.values('id', 'name') 
      # queryset = Product.objects.defer('unit_price') # چه چیز هایی رو نمیخام

      # select_related & prefetch_related

      # queryset = OrderItem.objects.select_related('product').all() # مربوط به فیلدی که ForeignKey خورده .
      # queryset = Product.objects.prefetch_related('order_items').all()  # برعکس بالایی عمل میکنه مثلا متد پروداکت در فایل مدل در کدوم اوردرایتم ها استفاده شده 
      # queryset = Comment.objects.select_related('product').all()
      # queryset = Product.objects.prefetch_related('comments').all()
      # queryset = Product.objects.select_related('category').prefetch_related('comments').all()
      # queryset = Order.objects.prefetch_related('items__product').select_related('customer').all()

      # aggregate & Count & Avg ...

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
      # queryset = OrderItem.objects.values('product_id').distinct() 

      # annotate & Value & F & Func
 
      # queryset = Product.objects.annotate(x=Value(1)).all()[:2] # تعریف ستون جدید بر اساس اون چیزی که ما میخوایم مثل ستون ایکس که تعریف کردیم (مقادیر محاسبه‌شده (مثل جمع، میانگین، یا شمارش) رو به هر شیء تو نتایج کوئری اضافه کنه)
      # queryset = Product.objects.annotate(price=F('unit_price')).all()[:2] # F() یه ابزار قدرتمند تو جنگوئه که برای کار با مقادیر فیلدهای مدل تو سطح دیتابیس استفاده می‌شه، بدون اینکه داده‌ها رو تو حافظه پایتون بارگذاری کنه. این برای به‌روزرسانی‌ها، مقایسه‌ها و محاسبات مستقیم تو دیتابیس عالیه. F = Field
      # queryset = OrderItem.objects.annotate(total_price=F('quantity') * F('unit_price')).all()
      # queryset = Customer.objects.annotate(fullname=Func(F('first_name'), Value(' '), F('last_name'), function='CONCAT')).defer('first_name', 'last_name')

      # group by

      # queryset = OrderItem.objects \
      #                     .values('order_id') \
      #                     .annotate(count=Count('order_id'))
      # queryset = Order.objects.annotate(items_count=Count('orderitem'))
      # queryset = Customer.objects.annotate(orders_count=Count('orders'))
      # queryset = Customer.objects.annotate(orders_count=Count('orders')).all()
      # queryset = Customer.objects.annotate(orders_count=Count('orders')).filter(id=17).all()

      # ExpressionWrapper - یه عبارت SQL پیچیده رو به‌عنوان یه فیلد جدید تو QuerySet تعریف کنی. این ابزار وقتی مفیده که بخوای عملیات‌هایی مثل ترکیب رشته‌ها، محاسبات ریاضی، یا شرط‌های سفارشی رو تو دیتابیس اجرا کنی.

      # queryset = OrderItem.objects.annotate(
      #       total_price=ExpressionWrapper(F('quantity') * F('unit_price'), output_field=DecimalField())
      # )
      # queryset = OrderItem.objects.annotate(
      #       total_price=ExpressionWrapper(F('unit_price') * 0.95, output_field=DecimalField())
      # )

      # Custom manager

      # queryset = Comment.objects.filter(status=Comment.COMMENT_STATUS_WAITING)

      # Custom manager method

      # queryset = Comment.approved.filter(datetime_create__year=2025).all()
      # print(queryset)
      # return render(request, 'hello.html' )

      # queryset = Order.objects.get_by_status(status=Order.ORDER_STATUS_UNPAID)
      # queryset = Order.objects.get_by_status(status='x')
      # queryset = Order.unpaid_orders.all()

      # make new object

      
      # product = Product.objects.get(id=1)
      # Comment.objects.create(
      #       name='samira',
      #       body='django is great. I love it.',
      #       product=product
      # )

      # Comment.objects.create(
      #       name='samira',
      #       body='django is great. I love it.',
      #       product_id=1,
      # )

      # product = Product.objects.get(id=1)
      # new_comment = Comment()
      # new_comment.name= 'Samira'
      # new_comment.body= 'I love to learn Django!'
      # new_comment.product= product
      # new_comment.save()

      # return render(request, 'hello.html' )

      # update objects

      # category = Category(id=100)
      # category.title = 'Cars'
      # category.description = 'This is the description for category'
      # category.save()

      # return render(request, 'hello.html' )

      # product = Product.objects.get(id=1)
      # category = Category(id=100)
      # category.title = 'Cars'
      # category.description = 'This is the description for category'
      # category.top_product_id = 2
      # category.save()

      # category = Category(pk=99)
      # category.top_product_id = 2
      # category.save()

      # category = Category.objects.get(pk=98)
      # category.top_product_id = 2
      # category.save()

      # Category.objects.filter(pk=97).update(title='A')

      # return render(request, 'hello.html' )

      # delete objects

      # Category.objects.create(title='SOME NEW TITLE')
      # Category.objects.filter(pk=101).delete()

      # cat = Category(pk=102)
      # cat.delete()

      # cat = Category.objects.create(title='Z', description='some description', top_product_id=1)
      
      # p1 = Product()
      # p1.name ='p1'
      # p1.category = cat
      # p1.slug = 'p-1'
      # p1.description = 'p1 description'
      # p1.unit_price = 1000
      # p1.inventory = 1
      # p1.save()

      # p2 = Product()
      # p2.name ='p2'
      # p2.category = cat
      # p2.slug = 'p-2'
      # p2.description = 'p2 description'
      # p2.unit_price = 2000
      # p2.inventory = 2
      # p2.save()

      # order = Order.objects.create(customer_id=1)

      # order_item1 = OrderItem.objects.create(
      #       order=order,
      #       product=p1,
      #       quantity=10,
      #       unit_price=p1.unit_price,
      # )

      # order_item2 = OrderItem.objects.create(
      #       order=order,
      #       product=p2,
      #       quantity=20,
      #       unit_price=p2.unit_price,
      # )

      # order_item3 = OrderItem.objects.create(
      #       order=order,
      #       product_id=1,
      #       quantity=30,
      #       unit_price=3000,
      # )

      # cat = Category.objects.earliest('-id')
      # cat.title = 'Q'
      # cat.save()

      # OrderItem.objects.filter(order_id=31).delete()
      # Order.objects.filter(id=31).delete()
      # Product.objects.filter(name__in=['p1', 'p2']).delete()
      # cat= Category.objects.earliest('-id')
      # cat.delete()

      # with transaction.atomic():
      #     order = Order.objects.create(customer_id=1)

      #     order_item1 = OrderItem.objects.create(
      #          order=order,
      #          product_id=1,
      #          quantity=10,
      #          unit_price=1000,
      #     )      

      # return render(request, 'hello.html' )

      
      # queryset = Product.objects.all()
      # print(queryset[2:4])

      # list(queryset)

      # اجرا sql  خام

      # cursor = connection.cursor()
      # cursor.execute('')
      # cursor.close()

      # with connection.cursor() as cursor:
      #       cursor.execute('')

      # Product.objects.raw('SELECT is, unit_price FROM store_product')

      # cursor = connection.cursor()
      # cursor.callproc('some_proc', 1, '2', 'hello')

      # queryset = Order.objects.prefetch_related('items') \
      #                         .annotate(
      #                               items_count=Count('items')
      #                         )
      # for order in queryset:
      #       print(order.items_count)


      # queryset = Order.objects.prefetch_related('items') \
      #                         .annotate(
      #                               items_count=Count('items')
      #                         )
      # for order in queryset:
      #       for order_item in order.items.all():
      #             print(order_item.product.name)
      # return render(request, 'hello.html' )


      # queryset = Order.objects.prefetch_related('items__product') \
      #                         .annotate(
      #                               items_count=Count('items')
      #                         )
      # for order in queryset:
      #       for order_item in order.items.all():
      #             print(order_item.product.name)
      # return render(request, 'hello.html' )

      # queryset = Order.objects.prefetch_related(
      #                         Prefetch(
      #                               'items',
      #                               queryset=OrderItem.objects.select_related('product')
      #                         )
      #                   ) \
      #                         .annotate(
      #                               items_count=Count('items')
      #                         )
      # for order in queryset:
      #       for order_item in order.items.all():
      #             print(order_item.product.name)

      return render(request, 'hello.html' )



      # print(list(queryset))
#       print([x.unit_price for x in list(queryset)])
      # print(len(list(queryset)))
      # list(queryset)
      # return render(request, 'hello.html', {'order_items': list(queryset) } )
#     return render(request, 'hello.html', {'customers': list(queryset)})
