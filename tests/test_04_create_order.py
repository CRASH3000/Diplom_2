import requests
import allure

@allure.story("4. Создание заказа")
class TestCreateOrder:
    endpoint_create_order = "/orders"
    endpoint_ingredients = "/ingredients"

    @allure.title("Создание заказа с авторизацией")
    def test_create_order_with_auth(self, base_url, auth_token, ingredients):
        headers = {"Authorization": auth_token}
        order_data = {"ingredients": ingredients[:2]}
        response = requests.post(base_url + self.endpoint_create_order, headers=headers, json=order_data)

        assert response.status_code == 200
        assert response.json().get("success") is True

    @allure.title("Создание заказа без авторизации")
    def test_create_order_without_auth(self, base_url, ingredients):
        order_data = {"ingredients": ingredients[:2]}
        response = requests.post(base_url + self.endpoint_create_order, json=order_data)

        assert response.status_code == 401
        assert response.json().get("message") == "You should be authorised"

    @allure.title("Создание заказа с ингредиентами")
    def test_create_order_with_ingredients(self, base_url, auth_token, ingredients):
        headers = {"Authorization": auth_token}
        order_data = {"ingredients": ingredients[:2]}
        response = requests.post(base_url + self.endpoint_create_order, headers=headers, json=order_data)

        assert response.status_code == 200
        assert response.json().get("success") is True
        assert "order" in response.json(), "Expected order data in response, but got none"

    @allure.title("Создание заказа с пустым списком ингредиентов")
    def test_create_order_with_ingredients_with_auth(self, base_url, auth_token, ingredients):
        headers = {"Authorization": auth_token}
        order_data = {"ingredients": ingredients[:2]}
        response = requests.post(base_url + self.endpoint_create_order, headers=headers, json=order_data)

        assert response.status_code == 200, "Expected status code 200, but got {}".format(response.status_code)
        assert response.json().get("success") is True, "Expected success to be True, but got False"
        assert "order" in response.json(), "Expected order data in response, but got none"

    @allure.title("Создание заказа с пустым списком ингредиентов без авторизации")
    def test_create_order_with_empty_ingredients_without_auth(self, base_url):
        order_data = {"ingredients": []}
        response = requests.post(base_url + self.endpoint_create_order, json=order_data)

        assert response.status_code == 401, "Expected status code 401, but got {}".format(response.status_code)
        assert response.json().get("message") == "You should be authorised", \
            "Expected message 'You should be authorised', but got '{}'".format(response.json().get("message"))

    @allure.title("Создание заказа с пустым списком ингредиентов")
    def test_create_order_no_ingredients(self, base_url, auth_token):
        headers = {"Authorization": auth_token}
        order_data = {"ingredients": []}
        response = requests.post(base_url + self.endpoint_create_order, headers=headers, json=order_data)

        assert response.status_code == 400
        assert response.json().get("message") == "Ingredient ids must be provided"

    @allure.title("Создание заказа с неверным хешем ингредиента")
    def test_create_order_invalid_ingredient_hash(self, base_url, auth_token):
        headers = {"Authorization": auth_token}
        order_data = {"ingredients": ["invalid_hash"]}
        response = requests.post(base_url + self.endpoint_create_order, headers=headers, json=order_data)

        assert response.status_code == 500
        assert response.json().get("message") == "Internal Server Error"