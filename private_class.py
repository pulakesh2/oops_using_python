class Employee:
    def __init__(self, name, address, email, id):
        # public variable
        self.name = name
        self.address = address

        # private variable
        self.__email = email
        self.__id = id


    # private method
    def __details(self):
        return f"employee name : {self.name}, address: {self.address}, email: {self.__email}, id: {self.__id}"

    # public method
    def print_details(self):
        return self.__details()



emp1 = Employee('pulakesh', 'guwahati', 'pulakesh', '01')
print(emp1.print_details())

