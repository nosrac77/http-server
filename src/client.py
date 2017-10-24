"""Function that contains client socket server function."""


import socket
client_socket = socket.socket(2, 1, 6)
client_socket.connect(('127.0.0.1', 6000))
client_socket.sendall('Message')
def client(message):
