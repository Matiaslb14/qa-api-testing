import requests

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_get_users_returns_200_and_list():
    r = requests.get(f"{BASE_URL}/users", timeout=10)

    assert r.status_code == 200
    data = r.json()

    assert isinstance(data, list)
    assert len(data) > 0

def test_user_structure_and_types():
    r = requests.get(f"{BASE_URL}/users", timeout=10)
    assert r.status_code == 200

    user = r.json()[0]

    assert "id" in user
    assert "name" in user
    assert "email" in user

    assert isinstance(user["id"], int)
    assert isinstance(user["name"], str)
    assert isinstance(user["email"], str)

def test_get_non_existing_endpoint_returns_404():
    r = requests.get(f"{BASE_URL}/users_not_exist", timeout=10)

    assert r.status_code == 404

def test_create_user_returns_201_and_echoes_payload():
    payload = {
        "name": "QA Mati",
        "username": "matiqa",
        "email": "matiqa@example.com"
    }

    r = requests.post(f"{BASE_URL}/users", json=payload, timeout=10)

    assert r.status_code in (200, 201)
    data = r.json()

    # JSONPlaceholder “simula” creación y suele devolver un id
    assert "id" in data
    assert data["name"] == payload["name"]
    assert data["username"] == payload["username"]
    assert data["email"] == payload["email"]