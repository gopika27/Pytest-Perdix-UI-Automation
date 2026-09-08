import json

def get_login_data():
    with open("test_data/login_data.json") as f:
        data = json.load(f)

    print("DATA READER:", data)
    return data