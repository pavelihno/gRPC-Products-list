from django_grpc_framework import generics

from products.models import Product
from products.serializers import ProductProtoSerializer


class ProductService(generics.ModelService):
    queryset = Product.objects.all()
    serializer_class = ProductProtoSerializer
