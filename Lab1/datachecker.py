import sqlite3
from customer import Customer

class DataChecker:
    def __init__(self):
        self.conn = sqlite3.connect('pos.db')
        self.cursor = self.conn.cursor()

    def check_valid_age(self, age):
        try:
            int(age)
        except ValueError:
            print('Non-valid integer input')
            return False

        if age < 0:
            print("Age can't be less than zero years old.")
            return False

        return True

    def check_valid_text_field(self, input, emptyTextNotAllowed=True):
        try:
            len(input)
        except TypeError:
            print('Non-valid string input')
            return False

        if len(input) <= 0 and emptyTextNotAllowed == True:
            print('Empty textfield not allowed')
            return False
        else:
            return True


    def customer_has_equipment_attached(self, customerID):
        self.cursor.execute("""SELECT * FROM Customers WHERE ID == ?;""", (customerID,))
        self.conn.commit()
        customers = self.cursor.fetchall()

        if len(customers) == 0:
            print("Customer ID not found in DB")
            return False

        customer = customers[0]
        tmp_customer = Customer(ID=customer[0], Firstname=customer[1], Lastname=customer[2], Age=customer[3], Sex=customer[4], Street=customer[5], Zip=customer[6], City=customer[7], Nationality=customer[8], IMSIPtr=customer[9], IMEIPtr=customer[10], SubscriptionPtr=customer[11], Email=customer[12], Password=customer[13])

        # Fetch equipment
        if tmp_customer.IMEIPtr != None:
            self.cursor.execute("""SELECT * FROM Equipment WHERE ID = ?;""", (tmp_customer.IMEIPtr,))
            self.conn.commit()
            equipment = self.cursor.fetchone()

            if len(equipment) == 0:
                print('Customer has equipment ID but ID cant be found in DB.')
                return False
            else:
                return True

        else:
            print('Customer has no equipment attached to profile.')
            return False
