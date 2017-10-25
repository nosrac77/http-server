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
            conn.close()

    except KeyboardInterrupt:
        server.close()
        sys.exit(1)


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


def parse_request(request):
    """Function that returns URI from client if conditions are met."""
    request = request.decode('utf8')
    if 'GET' != request[:3]:
        response_error(TypeError)
        raise(TypeError)
    if request.split()[2].split('\r\n')[0] != 'HTTP/1.1':
        response_error(TypeError)
        raise(TypeError)
    if request.split('\r\n')[1][:6] != 'Host: ':
        response_error(TypeError)
        raise(TypeError)
    return request.split()[1]


if __name__ == "__main__":
    start_server()
