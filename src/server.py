"""Function that creates a server to interact with client.py."""

import socket


def start_server():
    """Start the server."""
    server = socket.socket(2, 1, 6)

    server.bind(("127.0.0.1", 5678))

    server.listen(1)

    conn, addr = server.accept()
