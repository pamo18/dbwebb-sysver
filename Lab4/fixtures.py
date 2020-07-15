# Paul Moreland, pamo18
from pytest import fixture
from shutil import copy
from selenium import webdriver

# Setup up the Selenium webdriver
@fixture(scope="function")
def driver():
    driver = webdriver.Firefox()
    driver.get("http://127.0.0.1/")
    return driver

# Reset the db before each test
@fixture(scope="function", autouse=True)
def reset_db_before_each_test():
    reset_db()

# Reset db function
def reset_db():
    path = "/home/pft/restapi/point-of-sale/"
    copy(path + "pos_bak.db", path + "pos.db")
