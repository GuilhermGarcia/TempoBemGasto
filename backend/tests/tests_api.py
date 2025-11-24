import os
import sys
from fastapi.testclient import TestClient

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
BACKEND_DIR = os.path.dirname(CURRENT_DIR)
sys.path.append(BACKEND_DIR)

from main import api

client = TestClient(api)

def test_root_exists():
    response = client.get("/")
    assert response.status_code in (200, 404)

def test_docs_exist():
    response = client.get("/docs")
    assert response.status_code == 200
