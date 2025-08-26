import sys, os

# Add project root (where app.py is) to sys.path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import app   # Now Python can find app.py

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello, Jenkins CI/CD" in response.data
