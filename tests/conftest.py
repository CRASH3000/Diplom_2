import requests
import pytest
import uuid

@pytest.fixture(scope="session")
def base_url():
    return "https://stellarburgers.nomoreparties.site/api"

@pytest.fixture(scope="class")
def auth_token(base_url, request):
    unique_email = f"{uuid.uuid4()}@example.com"
    user_data = {
        "email": unique_email,
        "password": "securePassword123",
        "name": "OrderUser"
    }
    # Регистрация пользователя
    requests.post(base_url + "/auth/register", json=user_data)
    # Логин для получения токена
    response = requests.post(base_url + "/auth/login", json=user_data)
    token = response.json().get("accessToken")

    # Функция для удаления пользователя после тестов
    def delete_user():
        headers = {"Authorization": token}
        requests.delete(base_url + "/auth/user", headers=headers)

    request.addfinalizer(delete_user)
    return token

@pytest.fixture(scope="class")
def ingredients(base_url):
    response = requests.get(base_url + "/ingredients")
    ingredients = [item["_id"] for item in response.json().get("data", [])]
    return ingredients

@pytest.fixture(scope="class")
def unique_user_data(base_url, request):
    unique_email = f"{uuid.uuid4()}@example.com"
    user_data = {
        "email": unique_email,
        "password": "securePassword123",
        "name": "UniqueUser"
    }
    requests.post(base_url + "/auth/register", json=user_data)

    def delete_user():
        response = requests.post(base_url + "/auth/login", json=user_data)
        token = response.json().get("accessToken")
        headers = {"Authorization": token}
        requests.delete(base_url + "/auth/user", headers=headers)

    request.addfinalizer(delete_user)
    return user_data

@pytest.fixture(scope="class")
def create_order(base_url, auth_token, ingredients, request):
    headers = {"Authorization": auth_token}
    order_data = {"ingredients": ingredients[:2]}
    response = requests.post(base_url + "/orders", headers=headers, json=order_data)
    assert response.status_code == 200, "Order creation failed in fixture"
    order_id = response.json().get("order").get("number")

    def delete_order():
        requests.delete(base_url + f"/orders/{order_id}", headers=headers)

    request.addfinalizer(delete_order)
    return response.json()

@pytest.fixture(scope="class")
def persistent_user_data(base_url):
    """Фикстура для создания и возврата данных пользователя, который не удаляется после тестов."""
    email = "persistent_user@example.com"
    user_data = {
        "email": email,
        "password": "securePassword123",
        "name": "PersistentUser"
    }
    # Регистрация пользователя, если он еще не существует
    response = requests.post(base_url + "/auth/register", json=user_data)
    if response.status_code not in [200, 403]:
        response.raise_for_status()
    return user_data