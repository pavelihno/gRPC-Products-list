from products import product_pb2_grpc
from products.services import ProductService


def grpc_handlers(server):
    product_pb2_grpc.add_ProductControllerServicer_to_server(ProductService.as_servicer(), server)
