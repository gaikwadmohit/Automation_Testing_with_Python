
class CreateContacts:
    def __init__(self, first_name, last_name, address, city, state, pincode, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.pincode = pincode
        self.phone_number = phone_number
        self.email = email

    def person_input(self):

        self.first_name = input("Enter your First Name : ")
        self.last_name = input("Enter your Last Name : ")
        self.address = input("Enter your Address : ")
        self.city = input("Enter your City Name : ")
        self.state = input("Enter your State Name : ")
        self.pincode = int(input("Enter your Zip Code : "))
        self.phone_number = input("Enter your Phone Number : ")
        self.email = input("Enter your Email Address: ")
        return self.first_name, self.last_name, self.address, self.city, self.state, self.pincode, self.phone_number, self.email
        