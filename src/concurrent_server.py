"""Hold concurrent server."""
from server import start_server

if __name__ == '__main__':
    from gevent.server import StreamServer
    from gevent.monkey import patch_all
    patch_all()
    server = StreamServer(('127.0.0.1', 10000), start_server)
    print('Starting server on port 10000')
    server.serve_forever()
