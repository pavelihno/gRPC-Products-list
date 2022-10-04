import grpc

from products import product_pb2_grpc, product_pb2


with grpc.insecure_channel('localhost:50051') as channel:
    stub = product_pb2_grpc.ProductControllerStub(channel)

    response = stub.Create(product_pb2.Product(title='milk 1l', amount=2, is_bought=False))


"""
python manage.py shell --command="exec(open(r'client/create.py').read())"
"""
