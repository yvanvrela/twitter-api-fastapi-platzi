from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_create_user_ok():
    user = {
        'first_name': 'test_create_user',
        'last_name': 'test',
        'email': 'test@test.com',
        'birth_date': '1999-01-01',
        'password': 'secretpassword'
    }

    response = client.post(
        url='/api/v1/auth/signup/',
        json=user,
    )

    assert response.status_code == 201, response.text

    data = response.json()
    assert data['first_name'] == user['first_name']
    assert data['last_name'] == user['last_name']
    assert data['email'] == user['email']
    assert data['birth_date'] == user['birth_date']


def test_create_user_duplicate_email():

    user = {
        'first_name': 'test_create_user',
        'last_name': 'test',
        'email': 'test@test.com',
        'birth_date': '1999-01-01',
        'password': 'secretpassword'
    }

    response = client.post(
        url='/api/v1/auth/signup/',
        json=user,
    )

    assert response.status_code == 400, response.text
    data = response.json()
    assert data['detail'] == 'Email already registered'


def test_login():

    user_login = {
        'username': 'test@test.com',
        'password': 'secretpassword',
    }

    response = client.post(
        url='/api/v1/auth/login/',
        data=user_login,
        headers={
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        allow_redirects=True
    )

    assert response.status_code == 200, response.text

    data = response.json()
    assert len(data['access_token']) > 0
    assert data['token_type'] == 'bearer'
