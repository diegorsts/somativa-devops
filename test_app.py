import pytest
from app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_home_status(client):
    response = client.get("/")
    assert response.status_code == 200

def test_home_message(client):
    response = client.get("/")
    assert response.json["message"] == "Hello, DevOps!"

def test_health_status(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"

def test_info_fields(client):
    response = client.get("/info")
    data = response.json
    assert data["project"] == "somativa-devops"
    assert data["version"] == "1.0.0"
    assert data["author"] == "Diego Reis"

def test_info_content_type(client):
    response = client.get("/info")
    assert response.content_type == "application/json"

def test_sum(client):
    response = client.get("/sum/3/4")
    assert response.status_code == 200
    assert response.json["result"] == 7

def test_sum_zero(client):
    response = client.get("/sum/0/10")
    assert response.json["result"] == 10

def test_not_found(client):
    response = client.get("/rota-inexistente")
    assert response.status_code == 404
    assert response.json["error"] == "not found"
