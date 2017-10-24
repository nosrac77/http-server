"""Functions that test server and client socket functions."""


def test_server():
    """Function that tests the server function."""
    from server import start_server
    from client import start_client
    start_server()
    start_client('Hello')
    assert start_server() == 'Hello'
