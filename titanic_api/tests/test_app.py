from fastapi.testclient import TestClient
from app import app

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.json() == {"message": "Hello World!"}


def test_hello_name():
    response = client.get("/hello/Bob")
    assert response.json() == {"message": "Hello Bob!"}

def test_model_info():
    with TestClient(app) as client:
        response = client.get("/model")
        expected = {
            "dataset": "Titanic (Kaggle)",
            "classifier": "RandomForestClassifier",
            "accuracy": 0.782
            }
        assert response.json() == {"model": expected}
