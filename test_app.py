from app import app

def test_homepage():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"PawsSwipe" in response.data

def test_health_endpoint():
    client = app.test_client()
    response = client.get('/health')
    assert response.status_code == 200
    assert b"OK" in response.data