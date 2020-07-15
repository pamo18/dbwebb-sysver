# Paul Moreland, pamo18
import requests
import pytest
import time

from fixtures import api, reset_db
'''

'''
# Customer inserts per second
s = 1 / 10
end = 10

def test_create_customer(api):
    customer = {
        "Firstname": "Test",
        "Lastname": "Person",
        "Age": 39,
        "Sex": "Male",
        "Street": "Gata",
        "Zip": "123456",
        "City": "Någonstans",
        "Nationality": "Swedish",
        "Email": "lab8@någonmail.com",
        "Password": "pass"
    }

    # Start time
    start = time.perf_counter()

    while (time.perf_counter() - start) <= end:
        response = requests.post(api + "/customers", json=customer)
        result = response.json()

        assert response.status_code == 201
        assert result["Firstname"] == "Test"

        time.sleep(s)
