"""Function that creates a server to interact with client.py."""

import socket


def start_server():
    """Start the server."""
    server = socket.socket(2, 1, 6)
    server.bind(("127.0.0.1", 5678))

    server.listen(20)

    conn, addr = server.accept()

    buffer_length = 8

    message_complete = False

    entire_message = ""

    while not message_complete:
        part = conn.recv(buffer_length)
        print(part.decode('utf8'))
        conn.sendall(entire_message.decode('UTF8'))
        entire_message += part.decode('utf8')
        if len(part) < buffer_length:
            break

    conn.close()

    try:
        i = input('Press ctrl-d to exit.')
        if i == KeyboardInterrupt:
            conn.close()
            server.close()
        else:
            conn.sendall(entire_message.decode('UTF8'))
    except EOFError:
        conn.close()
        server.close()


if __name__ == "__main__":
    start_server()
