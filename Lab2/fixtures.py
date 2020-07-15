# Paul Moreland, pamo18
import pytest
import requests

# Setup up the API address
@pytest.fixture(scope="function")
def api():
    api = "http://127.0.0.1:6399"
    return api

# Find and remove the test customer
@pytest.fixture(scope="function")
def clean_customers():
    response = requests.get("http://127.0.0.1:6399/customers")
    result = response.json()
    testCustomer = next((index for (index, c) in enumerate(result) if c["Firstname"] == "Test"), None)

    if testCustomer != None:
        requests.delete("http://127.0.0.1:6399/customers/" + str(result[testCustomer]["ID"]))

# Find and remove the test sim
@pytest.fixture(scope="function")
def clean_sims():
    response = requests.get("http://127.0.0.1:6399/sims")
    result = response.json()
    testSim = next((index for (index, s) in enumerate(result) if s["IMSI"] == "IMSI_1122334455"), None)

    if testSim != None:
        requests.delete("http://127.0.0.1:6399/sims/" + str(result[testSim]["ID"]))

# Find and remove the test equipment
@pytest.fixture(scope="function")
def clean_equipments():
    response = requests.get("http://127.0.0.1:6399/equipments")
    result = response.json()
    testEquipment = next((index for (index, e) in enumerate(result) if e["IMEI"] == "IMEI_123456"), None)

    if testEquipment != None:
        requests.delete("http://127.0.0.1:6399/equipments/" + str(result[testEquipment]["ID"]))
