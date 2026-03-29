import requests
from typing import Tuple

def get_data(ip: str) -> Tuple[float, int]:
    try:
        response = requests.get(f"http://{ip}/data").json()
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        return None, None
    if response["temperature"] == 0:
        return None, None
    return response['temperature'], response['humidity']

