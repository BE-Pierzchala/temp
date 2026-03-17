import requests
from typing import Tuple

def get_data() -> Tuple[float, int, float]:
    response = requests.get("http://192.168.0.171/data").json()
    return response['temperature'], response['humidity'], response['heat_index']

