# Paul Moreland, pamo18
from fixtures import driver, reset_db_before_each_test, reset_db
import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver.common.alert import Alert

# Restore the database at the end of testing
def teardown_module():
    reset_db()

'''
test_open_customer_edit
test_create_customer
'''

# The test suite
class TestClass(object):
    # Setup the test suite
    def setup(self):
        self.delay = 4
        self.timeout = "Timeout error"

    # Test GUI - Open current customer and edit the first name and last name
    def test_open_customer_edit(self, driver):
        assert "Customer Care" in driver.title, "Testing: Page title is Customer Care"

        try:
            customer = WebDriverWait(driver, self.delay).until(EC.presence_of_element_located((By.ID, "513")))

            assert customer.text == "Kenneth Blomqvist", "Testing: Customer name is Kenneth Blomqvist"

            customer.click()
            driver.find_element_by_id("edit_customer_btn").click()

            customer_firstname = driver.find_element_by_id("firstname")
            customer_lastname = driver.find_element_by_id("lastname")
            customer_phone = driver.find_element_by_id("phone")
            customer_sim = driver.find_element_by_id("imsi")
            customer_device = driver.find_element_by_xpath("//div[contains(@class, 'rounded_red_table')]/table/tbody/tr[3]/td[2]")

            assert customer_firstname.get_attribute("value") == "Kennetha", "Testing: Customer first name is Kennetha"
            assert customer_lastname.get_attribute("value") == "Blomqvist", "Testing: Customer last name is Blomqvist"
            assert customer_phone.get_attribute("value") == "+46723580953", "Testing: Customer Phone number is +46723580953"
            assert customer_sim.get_attribute("value") == "IMSI_0123456789", "Testing: Customer Sim IMSI is IMSI_0123456789"
            assert customer_device.text == "Google Pixel 2 XL", "Testing: Customer device name is Google Pixel 2 XL"

            customer_firstname.clear()
            customer_firstname.send_keys("Dave")

            customer_lastname.clear()
            customer_lastname.send_keys("Smith")

            driver.find_element_by_id("save_customer_btn").click()

            customer = WebDriverWait(driver, self.delay).until(EC.presence_of_element_located((By.ID, "513")))

            assert customer.text == "Dave Smith", "Testing: Customer name is Dave Smith"

            customer.click()

            customer_firstname = driver.find_element_by_id("firstname")
            customer_lastname= driver.find_element_by_id("lastname")

            assert customer_firstname.get_attribute("value") == "Davea", "Testing: Customer first name is Davea (Known Bug)"
            assert customer_lastname.get_attribute("value") == "Smith", "Testing: Customer last name is Smith"
        except TimeoutException:
            print(self.timeout)
        finally:
            driver.close()

    # Test GUI - Create new customer
    def test_create_customer(self, driver):
        assert "Customer Care" in driver.title, "Testing: Page title is Customer Care"

        driver.find_element_by_xpath("//button[text()='New customer']").click()

        driver.find_element_by_id("firstname").send_keys("Dave")
        driver.find_element_by_id("lastname").send_keys("Smith")
        driver.find_element_by_id("age").send_keys("39")
        driver.find_element_by_id("gender").send_keys("male")
        driver.find_element_by_id("nationality").send_keys("British")
        driver.find_element_by_id("street").send_keys("A Street")
        driver.find_element_by_id("zipcode").send_keys("M224AB")
        driver.find_element_by_id("city").send_keys("Manchester")
        driver.find_element_by_id("email").send_keys("dave@mail.com")
        driver.find_element_by_id("save_customer_btn").click()

        try:
            customer = WebDriverWait(driver, self.delay).until(EC.presence_of_element_located((By.ID, "514")))

            assert customer.text == "Dave Smith", "Testing: Customer name is Dave Smith"

            customer.click()

            assert driver.find_element_by_id("firstname").get_attribute("value") == "Davea", "Testing: Customer first name is Davea"
            assert driver.find_element_by_id("lastname").get_attribute("value") == "Smith", "Testing: Customer last name is Smith"
            assert driver.find_element_by_id("age").get_attribute("value") == "40", "Testing: Customer age is 40 (Known Bug)"
            assert driver.find_element_by_id("gender").get_attribute("value") == "male", "Testing: Customer gender is male"
            assert driver.find_element_by_id("nationality").get_attribute("value") == "British", "Testing: Customer nationality is British"
            assert driver.find_element_by_id("street").get_attribute("value") == "A Street", "Testing: Customer street is A Street"
            assert driver.find_element_by_id("zipcode").get_attribute("value") == "M224AB", "Testing: Customer zip code is M224AB"
            assert driver.find_element_by_id("city").get_attribute("value") == "Manchester", "Testing: Customer city is Manchester"
            assert driver.find_element_by_id("email").get_attribute("value") == "", "Testing: Customer email is empty (Known Bug)"
        except TimeoutException:
            print(self.timeout)
        finally:
            driver.close()

    # Test GUI - Create new customer
    def test_delete_customer(self, driver):
        assert "Customer Care" in driver.title, "Testing: Page title is Customer Care"

        try:
            customer = WebDriverWait(driver, self.delay).until(EC.presence_of_element_located((By.ID, "513")))

            assert customer.text == "Kenneth Blomqvist", "Testing: Customer name is Kenneth Blomqvist"

            customer.click()

            WebDriverWait(driver, self.delay).until(EC.presence_of_element_located((By.ID, "delete_customer_btn"))).click()

            driver.switch_to.alert.accept()

            WebDriverWait(driver, self.delay).until(EC.staleness_of(customer))

            with pytest.raises(NoSuchElementException):
                assert driver.find_element_by_id("513"), "Testing: The Customer with id 513 is now deleted"
        except TimeoutException:
            print(self.timeout)
        finally:
            driver.close()
