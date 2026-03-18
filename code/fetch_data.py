import requests
from typing import Tuple

def get_data() -> Tuple[float, int, float]:
    try:
        response = requests.get("http://192.168.0.171/data").json()
    except (requests.exceptions.ConnectionError, requests.exceptions.Timeout):
        return None, None, None
    return response['temperature'], response['humidity'], response['heat_index']

