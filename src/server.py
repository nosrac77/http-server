"""Function that creates a server to interact with client.py."""


def response_ok(request):
    """Send back an HTTP 200 response."""
    import datetime
    file_extension = '.' + parse_request(request).split('.')[-1]
    response = "HTTP/1.1 200 OK\nDate: {}\n\r\n{}\nYour request was received.".format(datetime.datetime.now(), file_extension)
    print(response.encode())
    return response.encode()


def resolve_uri(uri):
    """Resolve a URI."""
    print(uri)
    try:
        if uri[-1] == '/':
            print(uri[-1])
            import HTML
            from os import listdir
            file_extension = '.' + uri.split('.')[-1]
            uri_directory = listdir(uri)
            htmlcode = HTML.list(uri_directory)
            return (htmlcode, file_extension)
        else:
            print('in else')
            file_extension = '.' + uri.split('.')[-1]
            import io
            with io.open(uri, encoding='utf-8') as f:
                file_contents = f.read()
                print('<body>' + file_contents + '</body>', file_extension)
                return ('<body>' + file_contents + '</body>', file_extension)
    except IOError:
        raise IOError('The file/directory you requested could not be found.')


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
        print(1)
        raise(TypeError)
    if request.split()[2][:8] != 'HTTP/1.1':
        print(request.split()[2][:8])
        print(2)
        raise(TypeError)
    if request.split()[2][12:18] != 'Host:':
        print(request.split()[2][12:18])
        print(3)
        raise(TypeError)
    return request.split()[1]


def start_server(socket, address):
    """Start the server."""
    import sys

    server = socket
    buffer_length = 8

    try:
        while True:
            entire_message = ''
            timer = True

            while timer:
                part = server.recv(buffer_length)
                print(part.decode('utf8'))
                entire_message += part.decode('utf8')

                if len(part) < buffer_length:
                    timer = False

            try:
                # import pdb; pdb.set_trace()
                print(response_ok(entire_message))
                print(resolve_uri(parse_request(entire_message)))
                server.sendall((response_ok(entire_message) + str(resolve_uri(parse_request(entire_message))).encode()))
            except TypeError:
                server.sendall(response_error(TypeError))

    except KeyboardInterrupt:
        server.close()
        sys.exit(1)


if __name__ == "__main__":
    start_server()
