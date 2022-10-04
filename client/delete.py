import grpc

from products import product_pb2_grpc, product_pb2


with grpc.insecure_channel('localhost:50051') as channel:
    stub = product_pb2_grpc.ProductControllerStub(channel)

    stub.Destroy(product_pb2.Product(id=2))


"""
python manage.py shell --command="exec(open(r'client/delete.py').read())"
"""
