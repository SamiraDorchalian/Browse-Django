from django.shortcuts import render
from django.http import HttpRequest

from .models import Product


def show_data(request):
    queryset = Product.objects.filter(id=1005)
    print(queryset.exists())
    # product = queryset.first()
    # print(product.id)
    # print(product.name)
    # print(product.unit_price)
    # print(len(q))
    # print(type(q))
    # print(list(q))
    # print(q[0])

    return render(request, 'hello.html')