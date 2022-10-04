from django_grpc_framework import proto_serializers

from products.models import Product
from products import product_pb2


class ProductProtoSerializer(proto_serializers.ModelProtoSerializer):
    class Meta:
        model = Product
        proto_class = product_pb2.Product
        fields = ['id', 'title', 'amount', 'is_bought']

    