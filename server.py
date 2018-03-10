import metric_pb2
import socket

sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)
sock.bind(('', 8888))

my_metric = metric_pb2.Metric()
data, addr = sock.recvfrom(1024)
my_metric.ParseFromString(data)
print(my_metric)
