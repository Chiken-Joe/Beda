import pytest
from API.auth_client import AuthClient
from API.booking_client import BookingClient
from Fixtures.auth_fixture import auth_token
from Fixtures.booking_factory import create_booking, valid_booking_payload, invalid_booking_payload

@pytest.fixture
def auth_client():
    return AuthClient()

@pytest.fixture
def booking_client(auth_token):
    client = BookingClient()
    client.set_auth_cookie(auth_token)
    return client

@pytest.fixture
def unauth_booking_client():
    return BookingClient()