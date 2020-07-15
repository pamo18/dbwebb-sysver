# Paul Moreland, pamo18
class Conn:
    def cursor(self):
        return Cursor()

    def commit(self):
        return True

class Cursor:
    def __init__(self):
        self.id = 0
        self.equipment = ""
        self.customers = [
            [
                1,
                "Firstname",
                "Lastname",
                30,
                "Male",
                "Street",
                "Zip",
                "City",
                "Nationality",
                "IMSIPtr",
                "IMEIPtr",
                "SubscriptionPtr",
                "Email",
                "Password"
            ]
        ]

    def execute(self, sql, params):
        if (isinstance(params[0], int)):
            self.id = params[0]
            self.customers[0][0] = self.id
        else:
            self.equipment = params[0]

        return True

    def fetchall(self):
        if self.id == 2:
            self.customers = []
        elif self.id == 3:
            self.customers[0][10] = ""
        elif self.id == 4:
            self.customers[0][10] = None

        return self.customers

    def fetchone(self):
        if self.equipment == "":
            return self.equipment

        return "equipment"
