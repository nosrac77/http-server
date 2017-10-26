"""Functions that test server and client socket functions."""


def test_response_ok_returns_response():
    """Function that tests reponse_ok function returns response."""
    from server import response_ok
    assert b"200" in response_ok()


def test_output_type_of_response_ok():
    """Test that the output is the correct type."""
    from server import response_ok
    assert isinstance(response_ok(), bytes)


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


def test_parse_request_correct_input():
    """Ensure that parse_request returns the URI given a correct input."""
    from server import parse_request
    good_input = "GET /path/to/index.html HTTP/1.1\r\nHost: www.mysite1.com:80\r\n\r\n"
    assert parse_request(good_input) == '/path/to/index.html'


def test_parse_request_incorrect_input():
    """Ensure that parse_request raises a TypeError given an incorrect input."""
    from server import parse_request
    import pytest
    with pytest.raises(TypeError):
        parse_request(b'bingbong')


def test_output_type_of_response_error():
    """Test that the output is the correct type."""
    from server import response_error
    assert type(response_error(TypeError)) == bytes


def test_output_of_response_error_exists():
    """Test that the output exists."""
    from server import response_error
    assert response_error(TypeError) is not None


def test_if_response_error_needs_inputs():
    """Test that the inputs are required."""
    from server import response_error
    import pytest
    with pytest.raises(TypeError):
        response_error()
