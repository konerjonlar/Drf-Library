from django.test import TestCase
from django.urls import reverse

# Create your tests here.
from rest_framework.test import APITestCase


class UserRegistrationTestCase(APITestCase):
    url = reverse("auth:profile")

    def test_user_registration(self):
        data = {
            "username": "kullanici",
            "email": "kullanici@hotmail.com",
            "password": "asdqd1",
        }
        response = self.client.post(self.url, data)
        self.assertEqual(201, response.status_code)
