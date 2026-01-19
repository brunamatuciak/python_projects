import time
import random
import requests

from config import GRAPHQL_URL, HEADERS, REQUEST_DELAY_MIN, REQUEST_DELAY_MAX
from utils.logger import info

def _sleep():
    time.sleep(random.uniform(REQUEST_DELAY_MIN, REQUEST_DELAY_MAX))

def graphql_request(payload):
    _sleep()
    response = requests.post(
        GRAPHQL_URL,
        headers=HEADERS,
        json=payload
    )
    response.raise_for_status()
    return response.json()
