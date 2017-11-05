"""Function that creates a server to interact with client.py."""

import socket


def start_server():
    """Start the server."""
    import sys

    server = socket.socket(2, 1, 6)
    server.bind(("127.0.0.1", 5678))
    server.listen(20)
    buffer_length = 8

    try:
        while True:
            conn, addr = server.accept()
            entire_message = ''
            timer = True

            while timer:
                part = conn.recv(buffer_length)
                print(part.decode('utf8'))
                entire_message += part.decode('utf8')

                if len(part) < buffer_length:
                    timer = False

                conn.sendall(entire_message)

    except KeyboardInterrupt:
        server.close()
        sys.exit(1)


if __name__ == "__main__":
    start_server()
