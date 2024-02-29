import grpc.cluster.cluster_pb2 as cluster__pb2
import grpc.cluster.cluster_pb2_grpc as cluster__pb2_grpc
import grpc

def call_grpc_function():
    # Create a gRPC channel to connect to the server
    channel = grpc.insecure_channel('localhost:50051')  # Adjust the address and port accordingly

    # Create a stub for the gRPC service
    stub = cluster__pb2_grpc.ClusterServiceStub(channel)

    # Create a request object
    request = cluster__pb2.Cluster()

    # Make the gRPC call and get the response
    response = stub.GeneratePriorityQueue(request)

    return response

print(call_grpc_function())