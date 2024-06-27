from django.db import IntegrityError
from django.test import TestCase

from accounts.models import User


class UserModelTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            email="test@example.com",
            password="Admin@12345678",
            first_name="Test",
            last_name="Test",
        )
        self.superuser = User.objects.create_superuser(
            email="admin@example.com",
            password="Admin@12345678",
            first_name="Admin",
            last_name="Admin",
        )

    def test_user_creation(self):
        self.assertTrue(self.user.is_authenticated)
        self.assertTrue(self.superuser.is_staff)
        self.assertTrue(self.superuser.is_superuser)

    def test_user_full_name(self):
        self.assertEqual(self.user.full_name, "Test Test")
        self.assertEqual(self.superuser.full_name, "Admin Admin")

    def test_user_email_uniqueness(self):
        with self.assertRaises(IntegrityError):
            User.objects.create_user(
                email="test@example.com",
                password="Admin@12345678",
                first_name="Test",
                last_name="Test",
            )