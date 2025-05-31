from decimal import Decimal
from rest_framework import serializers

from .models import Category, Product

class CategorySerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    description = serializers.CharField(max_length=500)


# class ProductSerializers(serializers.Serializer):
    # id = serializers.IntegerField()
    # name = serializers.CharField(max_length=255)
    # unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)
    # unit_price_after_tax = serializers.SerializerMethodField()
    # inventory = serializers.IntegerField()
    # # category = CategorySerializer()
    # category = serializers.HyperlinkedRelatedField(
    #     queryset=Category.objects.all(),
    #     view_name='category-detail',
    # )

    # def get_unit_price_after_tax(self, product):
    #     return round(product.unit_price * Decimal(1.09), 2)

class ProductSerializers(serializers.ModelSerializer):
    title = serializers.CharField(max_length=255, source='name')
    price = serializers.DecimalField(max_digits=6, decimal_places=2, source='unit_price')
    unit_price_after_tax = serializers.SerializerMethodField()
    category = serializers.HyperlinkedRelatedField(
        queryset=Category.objects.all(),
        view_name='category-detail',
    )

    class Meta:
        model = Product
        fields = ['id', 'title', 'category', 'price', 'inventory', 'unit_price_after_tax']
        # fields = '__all__'

    def get_unit_price_after_tax(self, product):
        return round(product.unit_price * Decimal(1.09), 2)
