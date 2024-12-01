
import os
import django

# Initialize Django settings
os.environ['DJANGO_SETTINGS_MODULE'] = 'vConfig.settings'
django.setup()

import random
from locust import HttpUser, task, between
from django.core.management import call_command
from userAccounts.models import *
from django.contrib.auth.hashers import make_password
from bs4 import BeautifulSoup


class SetupDatabase:
    @staticmethod
    def create_test_users():
        

        for i in range(1, 101):
            email = f"testuser{i}@example.com"
            password = "TestPassword123"
            if not Account.objects.filter(email=email).exists():
                Account.objects.create(
                    email=email,
                    password=make_password(password),
                    department='CECS',
                    verified=True,
                    first_name=f"Test",
                    last_name=f"User{i}"
                )

class LoginTestUser(HttpUser):
    wait_time = between(1, 3)

    @staticmethod
    def on_start():
        SetupDatabase.create_test_users()

    test_users = [{"email": f"testuser{i}@example.com", "password": "TestPassword123"} for i in range(1, 101)]

    @task
    def login(self):
        user = random.choice(self.test_users)

        # First, perform a GET request to fetch the login page and extract the CSRF token
        response = self.client.get("/login")
        soup = BeautifulSoup(response.text, 'html.parser')
        csrf_token = soup.find('input', {'name': 'csrfmiddlewaretoken'})['value']

        # Then, use the CSRF token in the POST request to login
        self.client.post("/login", data={
            "email": user["email"],
            "password": user["password"],
            "csrfmiddlewaretoken": csrf_token,
        }, headers={"Referer": "/login"})