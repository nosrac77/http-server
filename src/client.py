"""Function that contains client socket server function."""


def start_client(message):
    """Start the client."""
    import socket
    client_socket = socket.socket(2, 1, 6)
    client_socket.connect(('127.0.0.1', 5679))
    client_socket.sendall(message.encode('utf8'))
<<<<<<< HEAD

    buffer_length = 100
=======
    buffer_length = 8
>>>>>>> eb664115b48dff6ed7a973c996b4819b75f70c90

    entire_message = ''
    timer = True
    while timer:
        part = client_socket.recv(buffer_length)
        print(part.decode('utf8'))
        entire_message += part
        if len(part) < buffer_length:
<<<<<<< HEAD
            break
    client_socket.shutdown(socket.SHUT_WR)
=======
            timer = False

>>>>>>> eb664115b48dff6ed7a973c996b4819b75f70c90
    client_socket.close()


if __name__ == "__main__":
    import sys
    start_client(sys.argv[1])
    sys.exit()
