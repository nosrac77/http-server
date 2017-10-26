"""Function that creates a server to interact with client.py."""

import socket


def response_ok():
    """Send back an HTTP 200 response."""
    import datetime
    response = "HTTP/1.1 200 OK\nDate: {}\n\r\n\nYour message was received.".format(datetime.datetime.now())
    return response.encode()


def resolve_uri(uri):
    """Resolve a URI."""
    if uri[-1] == '/':
        import HTML
        from os import listdir
        uri_directory = listdir(uri)
        htmlcode = HTML.list(uri_directory)
        return htmlcode
    else:
        # file_extension = '.' + uri.split('.')[-1]
        # file_name = uri.split('/')[-1]
        import io
        with io.open(uri, encoding='utf-8') as f:
            file_contents = f.read()
            return file_contents


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
    if 'GET' != request[:3]:
        raise(TypeError)
    if request.split()[2] != 'HTTP/1.1':
        raise(TypeError)
    if request.split()[3] != 'Host:':
        raise(TypeError)
    resolve_uri(request.split()[1])
    return request.split()[1]


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

            try:
                parse_request(entire_message)
                conn.sendall(response_ok())
            except TypeError:
                conn.sendall(response_error(TypeError))

    except KeyboardInterrupt:
        server.close()
        sys.exit(1)


# if __name__ == "__main__":
#     start_server()
