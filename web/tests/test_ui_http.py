import requests

BASE_URL = "http://localhost:8000"

def test_valid_password():
    strong_pass = "SuperSecurePass12345!"
    response = requests.post(BASE_URL, data={"password": strong_pass}, allow_redirects=True)
    assert response.status_code == 200
    assert "Welcome" in response.text