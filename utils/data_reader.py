import json
import os


def get_login_data():

    # CI/CD environment
    if os.getenv("CI") == "true":

        return {
            "account_number": os.getenv("ACCOUNT_NUMBER"),
            "username": os.getenv("LOGIN_USERNAME"),
            "password": os.getenv("LOGIN_PASSWORD")
        }

    # Local execution
    with open("test_data/login_data.json") as f:
        return json.load(f)