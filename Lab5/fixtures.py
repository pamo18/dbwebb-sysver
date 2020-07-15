# Paul Moreland, pamo18
from pytest import fixture
from shutil import copy

# Setup up the API address
@fixture(scope="function")
def api():
    api = "http://127.0.0.1:6399"
    return api

# Reset the db before each test
@fixture(scope="function", autouse=True)
def reset_db():
    path = "/home/pft/restapi/point-of-sale/"
    copy(path + "pos_bak.db", path + "pos.db")
