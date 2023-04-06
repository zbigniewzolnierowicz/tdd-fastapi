from starlette.testclient import TestClient


def test_ping(test_app: TestClient):
    res = test_app.get("/ping")
    assert res.status_code == 200
    assert res.json() == {"environment": "dev", "ping": "pong!", "testing": True}
