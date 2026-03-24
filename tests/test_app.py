from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200
    assert b"Hello CI/CD" in response.data

def test_add():
    client = app.test_client()
    response = client.get("/add?a=2&b=3")
    json_data = response.get_json()
    assert response.status_code == 200
    assert json_data["result"] == 5