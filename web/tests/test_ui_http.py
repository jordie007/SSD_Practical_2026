"""UI testing over HTTP: exercises the running app via real HTTP requests
(no browser automation) against the URL given by APP_URL.
"""
import os
import requests

APP_URL = os.environ.get("APP_URL", "http://web:5000")


def test_home_page_has_login_form():
    resp = requests.get(APP_URL + "/")
    assert resp.status_code == 200
    assert "password" in resp.text.lower()
    assert "login" in resp.text.lower()


def test_common_password_stays_on_home():
    resp = requests.post(APP_URL + "/", data={"password": "iloveyou"})
    assert resp.status_code == 200
    assert "login" in resp.text.lower()


def test_valid_password_reaches_welcome():
    session = requests.Session()
    resp = session.post(
        APP_URL + "/", data={"password": "Xk9#mQz7pLwv"}, allow_redirects=True
    )
    assert resp.status_code == 200
    assert "welcome" in resp.text.lower()