"""Function that creates a server to interact with client.py."""

import socket


def start_server():
    """Start the server."""
    import sys
    server = socket.socket(2, 1, 6)
<<<<<<< HEAD
    server.bind(("127.0.0.1", 5679))

    server.listen(20)

    buffer_length = 100

    message_complete = False

    entire_message = ""

    while not message_complete:
        conn, addr = server.accept()
        part = conn.recv(buffer_length)
        entire_message += part.decode('utf8')
        if len(part) < buffer_length:
            break

    print(entire_message)

    conn.sendall(response_ok())

=======
    server.bind(("127.0.0.1", 5678))
    server.listen(20)
    buffer_length = 8
>>>>>>> eb664115b48dff6ed7a973c996b4819b75f70c90
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
            conn.close()
    except KeyboardInterrupt:
        server.close()
        sys.exit(1)


def response_ok():
    """Send back an HTTP 200 response."""
    import datetime
    response = "HTTP/1.1 200 OK\nDate: {}\n<CRLF>\nYour message was received.".format(datetime.datetime.now())

    return response.encode()


def response_error():
    """Send back an HTTP 500 response."""
    import datetime
    response = "HTTP/1.1 500 Internal Server Error\nDate: {}\n<CRLF>\nYour message was received.".format(datetime.datetime.now())

    return response.encode()


if __name__ == "__main__":
    start_server()
