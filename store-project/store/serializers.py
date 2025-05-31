from decimal import Decimal
from rest_framework import serializers

DOLLORS_TO_RIALS = 500000

class ProductSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField(max_length=255)
    unit_price = serializers.DecimalField(max_digits=6, decimal_places=2)
    # custome Serializer method field
    unit_price_after_tax = serializers.SerializerMethodField()
    inventory = serializers.IntegerField()
    # custome Serializer method field
    price_rials = serializers.SerializerMethodField()

    def get_price_rials(self, product):
        return int(product.unit_price * DOLLORS_TO_RIALS)

    def get_unit_price_after_tax(self, product):
        return round(product.unit_price * Decimal(1.09), 2)