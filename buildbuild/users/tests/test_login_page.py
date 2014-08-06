from django.test import TestCase
from django.test.client import Client

class LoginPageTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_login_page_request_should_return_200(self):
        response = self.client.get("/login/")
        self.assertEqual(response.status_code, 200)
