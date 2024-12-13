from fastapi.testclient import TestClient
from datetime import datetime


import pytest
from .main import app, DATE_FORMAT


client = TestClient(app)

"""
def test_home(): 
    response = client.get("/") 
    assert response.status_code == 200 
    assert "text/html" in response.headers["content-type"]
"""


def test_current_unix_code_and_utc_date():
    """Test the /api endpoint to get current UNIX timestamp and UTC date."""
    response = client.get("/api")
    assert response.status_code == 200

    data = response.json()
    assert "unix" in data
    assert "utc" in data

    # Validate the UNIX timestamp and UTC format
    now = datetime.now()
    expected_utc = now.strftime(DATE_FORMAT)

    assert abs(data["unix"] - int(now.timestamp())) <= 1  # Allow for slight time difference
    assert data["utc"] == expected_utc


def test_turn_timestamp_to_unix_date_code():
    """Test the /api/{dt} endpoint with a datetime input."""
    test_date = datetime(2024, 12, 12, 15, 30, 0)
    test_date_str = test_date.strftime("%Y-%m-%d %H:%M:%S")

    response = client.get(f"/api/{test_date_str}")
    assert response.status_code == 200

    data = response.json()
    assert "unix" in data
    assert "utc" in data

    assert data["unix"] == test_date.timestamp()
    assert data["utc"] == test_date.strftime(DATE_FORMAT)


def test_turn_unix_date_code_to_utc():
    """Test the /api/{unix_code} endpoint with a UNIX timestamp input."""
    test_unix = 1734010200  # Example UNIX timestamp
    expected_utc = datetime.utcfromtimestamp(test_unix).strftime(DATE_FORMAT)

    response = client.get(f"/api/{test_unix}")
    assert response.status_code == 200

    data = response.json()
    assert "unix" in data
    assert "utc" in data

    assert data["unix"] == test_unix
    assert data["utc"] == expected_utc


@pytest.mark.parametrize("invalid_input", [
    "not-a-date",
    ".12345.6789",
    "2024-99-99",
])
def test_invalid_datetime_input(invalid_input):
    """Test the /api/{dt} endpoint with invalid datetime input."""
    response = client.get(f"/api/{invalid_input}")
    assert response.status_code == 422  # Expecting a validation error

