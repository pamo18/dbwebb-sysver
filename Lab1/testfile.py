# Paul Moreland, pamo18
from datachecker import DataChecker
import mock
# Class to mock the db results
from conn import Conn

class TestClass(object):
    # Setup the test object
    # Override sqlite connect for mocked db results
    @mock.patch("datachecker.sqlite3.connect", return_value=Conn())
    def setup(self, mock_connect):
        self.dc = DataChecker()

    # Test valid age with a positive number
    def test_check_valid_age_valid(self):
        assert self.dc.check_valid_age(10) == True

    # Test invalid age with a negative number
    def test_check_valid_age_invalid(self):
        assert self.dc.check_valid_age(-1) == False

    # Test invalid age with a letter
    def test_check_valid_age_invalid_letter(self):
        assert self.dc.check_valid_age("d") == False

    # Test valid text with a string
    def test_check_valid_text_field_valid(self):
        assert self.dc.check_valid_text_field("hello") == True

    # Test invalid text with a number
    def test_check_valid_text_field_invalid(self):
        assert self.dc.check_valid_text_field(200) == False

    # Test valid text with empty string, allowed
    def test_check_valid_text_field_valid_empty(self):
        assert self.dc.check_valid_text_field("", False) == True

    # Test valid text with empty string, not allowed
    def test_check_valid_text_field_invalid_empty(self):
        assert self.dc.check_valid_text_field("") == False

    # Test valid customer with equipment, mock db results.
    def test_customer_has_equipment_attached_valid(self):
        assert self.dc.customer_has_equipment_attached(1) == True

    # Test valid invalid customer, mock db results.
    def test_customer_has_equipment_attached_invalid_id(self):
        assert self.dc.customer_has_equipment_attached(2) == False

    # Test valid customer with invalid equipment ID, mock db results.
    def test_customer_has_equipment_attached_invalid_equipment(self):
        assert self.dc.customer_has_equipment_attached(3) == False

    # Test valid customer with no equipment, mock db results.
    def test_customer_has_equipment_attached_invalid_equipment_none(self):
        assert self.dc.customer_has_equipment_attached(4) == False
