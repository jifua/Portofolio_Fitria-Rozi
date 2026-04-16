import requests

def test_get_posts(base_url):
    """TC-API-001: Get posts"""
    response = requests.get(f"{base_url}/posts")

    assert response.status_code == 200
    data = response.json()

    assert isinstance(data, list)
    assert len(data) > 0


def test_get_single_post(base_url):
    """TC-API-002: Get single post"""
    response = requests.get(f"{base_url}/posts/1")

    assert response.status_code == 200
    data = response.json()

    assert data["id"] == 1


def test_create_post(base_url):
    """TC-API-003: Create post"""
    payload = {
        "title": "QA Testing",
        "body": "Belajar API Testing",
        "userId": 1
    }

    response = requests.post(f"{base_url}/posts", json=payload)

    assert response.status_code == 201
    data = response.json()

    assert data["title"] == "QA Testing"


def test_delete_post(base_url):
    """TC-API-004: Delete post"""
    response = requests.delete(f"{base_url}/posts/1")

    assert response.status_code == 200