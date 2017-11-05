"""Function that creates a server to interact with client.py."""

import socket


def response_ok():
    """Send back an HTTP 200 response."""
    import datetime
    response = "HTTP/1.1 200 OK\nDate: {}\n\r\n\nYour message was received.".format(datetime.datetime.now())
    return response.encode()


def response_error(error):
    """Send back an HTTP 500 response."""
    import datetime
    if error is TypeError:
        response = "HTTP/1.1 400 Bad Request\nDate: {}\n\r\n\nYour message was received.".format(datetime.datetime.now())
    else:
        response = "HTTP/1.1 500 Internal Server Error\nDate: {}\n\r\n\nYour message was received.".format(datetime.datetime.now())
    return response.encode()


def start_server():
    """Start the server."""
    import sys

    server = socket.socket(2, 1, 6)
    server.bind(("127.0.0.1", 5679))
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

                conn.sendall(response_ok())
                conn.sendall(entire_message.encode())

    except KeyboardInterrupt:
        server.close()
        sys.exit(1)


if __name__ == "__main__":
    start_server()
