import os
import requests


BASE_URL = os.getenv(
    "BACKEND_URL",
    "http://localhost:8000"
)


def _auth_headers(token):
    return {
        "Authorization": f"Bearer {token}"
    }


def register_user(username, password):
    return requests.post(
        f"{BASE_URL}/register",
        json={
            "username": username,
            "password": password
        },
        timeout=10
    )


def login_user(username, password):
    return requests.post(
        f"{BASE_URL}/login",
        data={
            "username": username,
            "password": password
        },
        timeout=10
    )


def get_current_user(token):
    return requests.get(
        f"{BASE_URL}/me",
        headers=_auth_headers(token),
        timeout=10
    )


def process_lead(message):
    return requests.post(
        f"{BASE_URL}/process",
        json={
            "message": message
        },
        timeout=30
    )


def get_analytics(token):
    return requests.get(
        f"{BASE_URL}/analytics",
        headers=_auth_headers(token),
        timeout=10
    )


def get_recent_leads(token):
    return requests.get(
        f"{BASE_URL}/recent-leads",
        headers=_auth_headers(token),
        timeout=10
    )