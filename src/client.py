"""Function that contains client socket server function."""


def start_client(message):
    """Start the client."""
    import socket
    client_socket = socket.socket(2, 1, 6)
    client_socket.connect(('127.0.0.1', 5678))
    client_socket.sendall(message.encode('utf8'))
    buffer_length = 8
    entire_message = b''
    timer = True

    while timer:
        part = client_socket.recv(buffer_length)
        print(part.decode('utf8'))
        entire_message += part

        if len(part) < buffer_length:
            timer = False

    client_socket.close()


if __name__ == "__main__":
    import sys
    start_client(sys.argv[1])
