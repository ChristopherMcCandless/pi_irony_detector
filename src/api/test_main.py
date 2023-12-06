from fastapi.testclient import TestClient
from src.api.main import app

def test_detect_text_result_should_be_irony():
    with TestClient(app) as client:
        response = client.post(
            "/detect-irony/", 
            json={"text_to_detect": "that's my dream to do my homework all night"})

        assert response.status_code == 200
        assert response.json()["irony"] > 0.8
        assert response.json()["non-irony"] <= 0.2

def test_detect_text_result_should_be_non_irony():
    with TestClient(app) as client:
        response = client.post(
            "/detect-irony/", 
            json={"text_to_detect": "you are absolutely right!"})

        assert response.status_code == 200
        assert response.json()["irony"] <= 0.5
        assert response.json()["non-irony"] > 0.5