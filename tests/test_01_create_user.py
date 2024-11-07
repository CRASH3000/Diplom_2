import requests
import allure

@allure.story("1. Создание пользователя")
class TestCreateUser:
    endpoint = "/auth/register"

    @allure.title("Создание уникального пользователя")
    def test_create_unique_user(self, base_url, unique_user_data):
        response = requests.post(base_url + self.endpoint, json=unique_user_data)

        assert response.status_code == 200
        assert response.json().get("success") is True
        assert "accessToken" in response.json()
        assert "refreshToken" in response.json()

    @allure.title("Создание пользователя, который уже зарегистрирован")
    def test_create_existing_user(self, base_url, persistent_user_data):
        response = requests.post(base_url + self.endpoint, json=persistent_user_data)

        assert response.status_code == 403
        assert response.json().get("message") == "User already exists"

    @allure.title("Создание пользователя с пропуском обязательного поля")
    def test_create_user_missing_field(self, base_url):
        data = {
            "email": "new_user_missing_field@example.com",
            "password": "securePassword123"
            # Отсутствует поле "name"
        }
        response = requests.post(base_url + self.endpoint, json=data)

        assert response.status_code == 403
        assert response.json().get("message") == "Email, password and name are required fields"