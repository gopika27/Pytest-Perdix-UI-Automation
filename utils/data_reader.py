import json
import os


def get_login_data():

    if os.getenv("CI") == "true":
        data = {
            "account_number": os.getenv("ACCOUNT_NUMBER"),
            "username": os.getenv("LOGIN_USERNAME"),
            "password": os.getenv("LOGIN_PASSWORD")
        }

        print("CI credentials loaded:")
        print("Account number present:", bool(data["account_number"]))
        print("Username present:", bool(data["username"]))
        print("Password present:", bool(data["password"]))

        return data

    with open("test_data/login_data.json") as f:
        return json.load(f)