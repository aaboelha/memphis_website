import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_home():
    response = client.get("/")
    assert response.status_code == 200
    assert "Memphis" in response.text

def test_portfolio():
    response = client.get("/portfolio")
    assert response.status_code == 200
    assert "Portfolio" in response.text

def test_about():
    response = client.get("/about")
    assert response.status_code == 200
    assert "About" in response.text

def test_contact():
    response = client.get("/contact")
    assert response.status_code == 200
    assert "Contact" in response.text
