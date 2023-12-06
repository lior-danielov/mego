class Customer:
    def __init__(self, contact_data):
        self.contact_data = contact_data

    def add_custom(self,customer_name, name ,phone, mail):
        with open(customer_name, mode="a+") as file:
            file.write(name, phone, mail)

    def list_customers(self):
        pass

    def looking_for(self):
        pass

    def set_info(self):
        pass

customer_name = "my_file.txt"
customer1 = Customer("my_file.txt")
# contact_manager = ContactManager("contact_list.txt”)
customer1.add_custom(customer_name, "John","555-1234","john@gmail.com")
# contact_manager.read_contact_list()
# contact manager.search contact(“John”)
# contact_manager.update_infromation(“John”,”555-1111”,”Jhon@walla.com”)