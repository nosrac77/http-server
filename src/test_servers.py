"""Functions that test server and client socket functions."""


def test_server():
    """Function that tests the server function."""
    from server import start_server
    from client import start_client
    start_server()
    start_client('Hello')
    assert start_server() == 'Hello'


def test_response_ok_returns_response():
    """Function that tests reponse_ok function returns response."""
    from server import response_ok
    assert response_ok().contains('200')


def test_output_type_of_response_ok():
    """Test that the output is the correct type."""
    from server import response_ok
    assert response_ok() == str


def test_output_of_response_ok_exists():
    """Test that the output exists."""
    from server import response_ok
    assert response_ok() is not None


def test_if_response_ok_needs_no_inputs():
    """Test that an unnecessary parameter will raise a TypeError."""
    from server import response_ok
    import pytest
    with pytest.raises(TypeError):
        response_ok(5)


def test_response_error_returns_response():
    """Function that tests reponse_error function returns response."""
    from server import response_error
    assert response_error().contains('500')


def test_output_type_of_response_error():
    """Test that the output is the correct type."""
    from server import response_error
    assert response_error() == str


def test_output_of_response_error_exists():
    """Test that the output exists."""
    from server import response_error
    assert response_error() is not None


def test_if_response_error_needs_no_inputs():
    """Test that an unnecessary parameter will raise a TypeError."""
    from server import response_error
    import pytest
    with pytest.raises(TypeError):
        response_error(5)
