from rest_framework.test import APIClient, APITestCase


class UserChangePasswordTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = self.client.post(
            "/accounts/register/",
            {
                "email": "test@example.com",
                "password": "Admin@12345678",
                "first_name": "Test",
                "last_name": "Test",
            },
            format="json",
        )
        self.token = self.client.post(
            "/accounts/token/",
            {"email": "test@example.com", "password": "Admin@12345678"},
            format="json",
        ).json()["access"]

    def test_change_password(self):
        data = {
            "old_password": "Admin@12345678",
            "new_password": "Admin@12345679",
            "confirm_password": "Admin@12345679",
        }
        response = self.client.patch(
            "/accounts/change-password/",
            data,
            format="json",
            HTTP_AUTHORIZATION="Bearer " + self.token,
        )
        self.assertEqual(response.status_code, 200)
