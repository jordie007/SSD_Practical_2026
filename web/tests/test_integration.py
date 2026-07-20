"""Integration test: password validation + Flask routes + session, working together."""
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from app import app


def test_common_password_rejected():
    client = app.test_client()
    resp = client.post("/", data={"password": "password123456"})
    assert resp.status_code == 200
    assert b"Login" in resp.data


def test_short_password_rejected():
    client = app.test_client()
    resp = client.post("/", data={"password": "short1"})
    assert resp.status_code == 200
    assert b"Login" in resp.data


def test_valid_password_reaches_welcome():
    client = app.test_client()
    resp = client.post("/", data={"password": "Xk9#mQz7pLwv"}, follow_redirects=True)
    assert resp.status_code == 200
    assert b"Welcome" in resp.data


def test_logout_clears_session():
    client = app.test_client()
    client.post("/", data={"password": "Xk9#mQz7pLwv"})
    client.post("/logout")
    resp = client.get("/welcome", follow_redirects=True)
    assert b"Login" in resp.data