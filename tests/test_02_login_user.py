import requests
import allure

@allure.story("2. Логин пользователя")
class TestLoginUser:
    endpoint_login = "/auth/login"

    @allure.title("Логин под существующим пользователем")
    def test_login_existing_user(self, base_url, persistent_user_data):
        response = requests.post(base_url + self.endpoint_login, json=persistent_user_data)

        assert response.status_code == 200
        assert response.json().get("success") is True
        assert "accessToken" in response.json()

    @allure.title("Логин с неверным логином и паролем")
    def test_login_incorrect_credentials(self, base_url):
        incorrect_data = {
            "email": "nonexistent_user@example.com",
            "password": "wrongPassword"
        }
        response = requests.post(base_url + self.endpoint_login, json=incorrect_data)

        assert response.status_code == 401
        assert response.json().get("message") == "email or password are incorrect"