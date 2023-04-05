import json

from fastapi import FastAPI

def test_create_summary(test_app_with_db: FastAPI):
    response = test_app_with_db.post("/summaries/", content=json.dumps({"url": "https://foo.bar"}))

    assert response.status_code == 201
    assert response.json()["url"] == "https://foo.bar"