from rest_framework.test import APIClient, APITestCase

from accounts.models import User


class UserRegisterTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="test@example.com",
            password="Admin@1234567",
            first_name="Test",
            last_name="Test",
        )

    def test_register_user(self):
        data = {
            "email": "test1@example.com",
            "password": "Admin@12345678",
            "first_name": "Test",
            "last_name": "Test",
        }
        response = self.client.post("/accounts/register/", data)
        self.assertEqual(response.status_code, 201)

    def test_register_user_with_existing_email(self):
        data = {
            "email": "test@example.com",
            "password": "Admin@12345678",
            "first_name": "Test",
            "last_name": "Test",
        }
        response = self.client.post("/accounts/register/", data)
        self.assertEqual(response.status_code, 400)

    def test_register_user_with_short_password(self):
        data = {
            "email": "test3@example.com",
            "password": "123",
            "first_name": "Test",
            "last_name": "Test",
        }
        response = self.client.post("/accounts/register/", data)
        self.assertEqual(response.status_code, 400)

    def test_register_user_with_no_password(self):
        data = {"email": "test4@example.com", "first_name": "Test", "last_name": "Test"}
        response = self.client.post("/accounts/register/", data)
        self.assertEqual(response.status_code, 400)
