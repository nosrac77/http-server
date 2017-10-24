"""Function that contains client socket server function."""


def start_client(message):
    """Start the client."""
    import socket
    client_socket = socket.socket(2, 1, 6)
    client_socket.connect(('127.0.0.1', 5678))
    client_socket.sendall(message.encode('utf8'))

if __name__ == "__main__":
    import sys
    start_client(sys.argv[1])
