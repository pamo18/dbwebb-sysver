# Paul Moreland, pamo18
import requests
import pytest
import time
from httperfpy import Httperf

from fixtures import api, reset_db
'''

'''

# Start time
start = time.perf_counter()
# Customer inserts per second
s = 1 / 100
end = 5

def test_get_customer1(api):
    while (time.perf_counter() - start) <= end:
        response = requests.get(api + "/customers")
        assert response.status_code == 200
        time.sleep(s)

def test_get_customer2(api):
    while (time.perf_counter() - start) <= end:
        response = requests.get(api + "/customers")
        assert response.status_code == 200
        time.sleep(s)

def test_get_customer3(api):
    while (time.perf_counter() - start) <= end:
        response = requests.get(api + "/customers")
        assert response.status_code == 200
        time.sleep(s)

def test_get_customer4(api):
    while (time.perf_counter() - start) <= end:
        response = requests.get(api + "/customers")
        assert response.status_code == 200
        time.sleep(s)

def test_get_customer4(api):
    while (time.perf_counter() - start) <= end:
        response = requests.get(api + "/customers")
        assert response.status_code == 200
        time.sleep(s)

def test_get_customer5(api):
    while (time.perf_counter() - start) <= end:
        response = requests.get(api + "/customers")
        assert response.status_code == 200
        time.sleep(s)
