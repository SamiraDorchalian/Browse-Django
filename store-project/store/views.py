from django.shortcuts import get_object_or_404

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Product
from .serializers import ProductSerializers

@api_view()
def product_list(request):
    return Response('Hello')

@api_view()
def product_detail(request, id):
    product = get_object_or_404(Product, pk=id)
    # try:
    #     product = Product.objects.get(pk=id) #get data from database
    # except Product.DoesNotExist:
    #     return Response(status=status.HTTP_404_NOT_FOUND) #If there was no data

    serializer = ProductSerializers(product) # Data processing to change format
    return Response(serializer.data) # Deliver data to the user in JSON format