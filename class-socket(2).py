from socket import *

Host = '127.0.0.1'
Port = 9999

client_socket = socket(AF_INET, SOCK_STREAM)

client_socket.connect((Host, Port))
client_socket.recv(1024)

data = client_socket.recv(1024)
print('Received from', repr(data.decode()))

client_socket.close()