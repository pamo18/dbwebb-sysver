# Paul Moreland, pamo18
import requests
import pytest
from fixtures import api, clean_customers, clean_sims, clean_equipments
'''
test_create_customer
test_create_sim
test_update_customer_new_sim
test_create_equipment
test_update_customer_new_equipment
'''
class TestClass(object):
    # Test to create a new customer
    def test_create_customer(self, api, clean_customers):
        customer = {
            "Firstname": "Test",
            "Lastname": "Moreland",
            "Age": 39,
            "Sex": "Male",
            "Street": "Ringvägen",
            "Zip": "123456",
            "City": "Västra Götaland",
            "Nationality": "Swedish",
            "Email": "pauljm80@gmail.com",
            "Password": "pass"
        }

        response = requests.post(api + "/customers", json=customer)
        result = response.json()

        assert response.status_code == 201
        assert result["Firstname"] == "Test"

    # Test to create a new sim
    def test_create_sim(self, api, clean_sims):
        sim = {
            "IMSI": "IMSI_1122334455",
            "MSISDN": "+46701214567"
        }

        response = requests.post(api + "/sims", json=sim)
        result = response.json()

        assert response.status_code == 201
        assert result["IMSI"] == "IMSI_1122334455"
        assert result["MSISDN"] == "+46701214567"

    # Test to update the new customer and add the new sim
    def test_update_customer_new_sim(self, api):
        customer_response = requests.get("http://127.0.0.1:6399/customers")
        customer_result = customer_response.json()
        customer_index = next((index for (index, c) in enumerate(customer_result) if c["Firstname"] == "Test"), None)
        customer = customer_result[customer_index]

        sim_response = requests.get("http://127.0.0.1:6399/sims")
        sim_result = sim_response.json()
        sim_index = next((index for (index, s) in enumerate(sim_result) if s["IMSI"] == "IMSI_1122334455"), None)
        sim = sim_result[sim_index]

        updatedCustomer = {
            "Firstname": "Test",
            "Lastname": "Moreland",
            "Age": 39,
            "Sex": "Male",
            "Street": "Ringvägen",
            "Zip": "123456",
            "City": "Västra Götaland",
            "Nationality": "Swedish",
            "IMSIPtr": str(sim["ID"])
        }

        response = requests.put(api + "/customers/" + str(customer["ID"]), json=updatedCustomer)
        result = response.json()

        assert response.status_code == 200

        response = requests.get(api + "/customers/" + str(customer["ID"]))
        result = response.json()

        assert customer_response.status_code == 200
        assert sim_response.status_code == 200
        assert customer_index != None
        assert sim_index != None
        assert result["Firstname"] == "Test"
        assert result["IMSIPtr"] == sim["ID"]

    # Test to create a new equipment with an already created product
    def test_create_equipment(self, api, clean_equipments):
        product_response = requests.get(api + "/products")
        product_result = product_response.json()
        product = product_result[0]

        equipment = {
            "IMEI": "IMEI_123456",
            "ProductPtr": product["ID"],
        }

        response = requests.post(api + "/equipments", json=equipment)
        result = response.json()

        assert response.status_code == 201
        assert result["IMEI"] == "IMEI_123456"
        assert result["ProductPtr"] == product["ID"]

    # Test to update the new customer and add the new equipment
    def test_update_customer_new_equipment(self, api):
        customer_response = requests.get("http://127.0.0.1:6399/customers")
        customer_result = customer_response.json()
        customer_index = next((index for (index, c) in enumerate(customer_result) if c["Firstname"] == "Test"), None)
        customer = customer_result[customer_index]

        equipment_response = requests.get("http://127.0.0.1:6399/equipments")
        equipment_result = equipment_response.json()
        equipment_index = next((index for (index, e) in enumerate(equipment_result) if e["IMEI"] == "IMEI_123456"), None)
        equipment = equipment_result[equipment_index]

        updatedCustomer = {
            "Firstname": "Test",
            "Lastname": "Moreland",
            "Age": 39,
            "Sex": "Male",
            "Street": "Ringvägen",
            "Zip": "123456",
            "City": "Västra Götaland",
            "Nationality": "Swedish",
            "IMEIPtr": str(equipment["ID"])
        }

        response = requests.put(api + "/customers/" + str(customer["ID"]), json=updatedCustomer)
        result = response.json()

        assert response.status_code == 200

        response = requests.get(api + "/customers/" + str(customer["ID"]))
        result = response.json()

        assert customer_response.status_code == 200
        assert equipment_response.status_code == 200
        assert customer_index != None
        assert equipment_index != None
        assert result["Firstname"] == "Test"
        assert result["IMEIPtr"] == equipment["ID"]
