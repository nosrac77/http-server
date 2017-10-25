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
    response = "HTTP/1.1 200 OK\nDate: {}\n<CRLF>\nYour message was received.".format(datetime.datetime.now())
    return response.encode()


def response_error():
    """Send back an HTTP 500 response."""
    import datetime
    response = "HTTP/1.1 500 Internal Server Error\nDate: {}\n<CRLF>\nYour message was received.".format(datetime.datetime.now())
    return response.encode()


def parse_request(request):
    """Function that returns URI from client if conditions are met."""
    request = request.decode('utf8')
    if 'GET' != request[:3]:
        print('I')
        raise(TypeError)
    if request.split()[2].split('<CRLF>')[0] != 'HTTP/1.1':
        print('you')
        raise(TypeError)
    if request.split('<CRLF>')[1][:6] != 'Host: ':
        print('me')
        raise(TypeError)
    print(request.split()[1])
    return request.split()[1]


if __name__ == "__main__":
    start_server()
