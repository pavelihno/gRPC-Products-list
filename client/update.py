import grpc

from products import product_pb2_grpc, product_pb2


with grpc.insecure_channel('localhost:50051') as channel:
    stub = product_pb2_grpc.ProductControllerStub(channel)

    print('connected')

"""
python manage.py shell --command="exec(open(r'client/update.py').read())"
"""