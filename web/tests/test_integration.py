import requests
import pytest

BASE_URL = "http://localhost:8000"

def test_home_page():
    response = requests.get(BASE_URL)
    assert response.status_code == 200