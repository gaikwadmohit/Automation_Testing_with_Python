from contact import CreateContacts


class AddressBook:
    addressbook = []

    def add_person(self, dict_person):

        fname = dict_person.get("First Name")
        lname = dict_person.get("Last Name")
        address = dict_person.get("Address")
        city = dict_person.get("City")
        state = dict_person.get("State")
        pincode = dict_person.get("Pincode")
        phone_number = dict_person.get("Phone Number")
        email = dict_person.get("Email")
        add = CreateContacts(first_name=fname, last_name=lname, address=address, city=city, state=state,
                             pincode=pincode, phone_number=phone_number, email=email)

        self.addressbook.append(add)
        return self.addressbook

    def display_person(self):

        i = 1
        print("Contact details present in Address Book : ")
        for detail in self.addressbook:
            print(f"\nRecord - {i}")
            print(f"First name : {detail.first_name}")
            print(f"Last name : {detail.last_name}")
            print(f"Address : {detail.address}")
            print(f"City : {detail.city}")
            print(f"State : {detail.state}")
            print(f"Pincode : {detail.pincode}")
            print(f"Phone Number : {detail.phone_number}")
            print(f"Email : {detail.email}")
            i += 1