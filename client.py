import metric_pb2
import socket
import sys
import time

my_metric = metric_pb2.Metric()
my_metric.name = 'sys.cpu'
my_metric.type = 'gauge'
my_metric.value = 99.9
my_metric.tags = "tags"
encoded = my_metric.SerializeToString()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET,
                     socket.SOCK_DGRAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 8888)
sock.connect(server_address)
sock.sendall(encoded)
time.sleep(5)
sock.close()
