import requests
import allure

@allure.story("3. Изменение данных пользователя")
class TestUpdateUser:
    endpoint_update_user = "/auth/user"

    @allure.title("Изменение данных с авторизацией")
    def test_update_user_with_auth(self, base_url, auth_token):
        headers = {"Authorization": auth_token}
        update_data = {"name": "UpdatedName"}
        response = requests.patch(base_url + self.endpoint_update_user, headers=headers, json=update_data)

        assert response.status_code == 200
        assert response.json().get("user").get("name") == "UpdatedName"

    @allure.title("Изменение данных без авторизации")
    def test_update_user_without_auth(self, base_url):
        update_data = {"name": "NoAuthName"}
        response = requests.patch(base_url + self.endpoint_update_user, json=update_data)

        assert response.status_code == 401
        assert response.json().get("message") == "You should be authorised"