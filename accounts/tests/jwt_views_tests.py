from rest_framework.test import APIClient, APITestCase

from accounts.models import User


class UserJWTViewsTest(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            email="test@example.com",
            password="Admin@12345678",
            first_name="Test",
            last_name="Test",
        )

    def test_obtain_token(self):
        data = {"email": "test@example.com", "password": "Admin@12345678"}
        response = self.client.post("/accounts/token/", data, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)
    
    def test_obtain_token_invalid_credentials(self):
        data = {"email": "test@example.com", "password": "wrong_password"}
        response = self.client.post("/accounts/token/", data, format="json")
        self.assertEqual(response.status_code, 401)
        self.assertNotIn("access", response.data)
        self.assertNotIn("refresh", response.data)
    
    def test_verify_token(self):
        data = {"email": "test@example.com", "password": "Admin@12345678"}
        access_token = self.client.post("/accounts/token/", data, format="json").data.get("access")
        data = {"token": access_token}
        response = self.client.post("/accounts/token/verify/", data, format="json")
        self.assertEqual(response.status_code, 200)
        
    def test_refresh_token(self):
        data = {"email": "test@example.com", "password": "Admin@12345678"}
        tokens = self.client.post("/accounts/token/", data, format="json").data
        data = {"refresh": tokens.get("refresh")}
        response = self.client.post("/accounts/token/refresh/", data, format="json")
        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)
        self.assertNotIn("refresh", response.data)