import json


def save_cookie(cookie: dict) -> None:
    with open('data/cookie.json', 'w') as file:
        json.dump(cookie, file, indent=4)


def get_cookie() -> dict:
    with open('data/cookie.json', 'r') as file:
        return json.load(file)
