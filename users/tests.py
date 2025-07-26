from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework.test import APITestCase

# Create your tests here.


class AuthTestCase(APITestCase):
    def setUp(self):
        self.register_url = reverse("auth_register")
        self.token_url = reverse("token_obtain_pair")

    def test_user_registration(self):
        data = {
            "username": "testuser",
            "email": "test@mail.com",
            "password": "StrongPass123",
            "password2": "StrongPass123",
            "first_name": "Test",
            "last_name": "User",
        }

        response = self.client.post(self.register_url, data)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)

    def test_user_login_with_token(self):
        User.objects.create_user(username="loginuser", password="12345")
        data = {"username": "loginuser", "password": "12345"}
        response = self.client.post(self.token_url, data)
        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_invalid_login(self):
        data = {"username": "wrong", "password": "wrongpass"}
        response = self.client.post(self.token_url, data)
        self.assertEqual(response.status_code, 401)

    def test_token_verification(self):
        User.objects.create_user(username="verifyuser", password="verify123")
        token_resp = self.client.post(
            self.token_url, {"username": "verifyuser", "password": "verify123"}
        )
        access = token_resp.data["access"]
        verify_url = reverse("token_verify")
        response = self.client.post(verify_url, {"token": access})
        self.assertEqual(response.status_code, 200)
