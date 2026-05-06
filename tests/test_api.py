# tests/test_api.py

from app.api import app

def test_set_speed_api():
    client = app.test_client()

    response = client.post("/set_speed", json={"speed": 80})

    assert response.status_code == 200
    assert response.get_json()["msg"] == "sent"


def test_ecu2_status_api():
    client = app.test_client()

    response = client.get("/ecu2")

    assert response.status_code == 200
    data = response.get_json()

    assert "speed" in data
    assert "brake" in data