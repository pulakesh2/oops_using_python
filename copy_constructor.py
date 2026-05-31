class Student():
    def __init__(self, name = None, address = None, email = None, other = None):
        if other:
            self.__name = other.__name
            self.__address = other.__address
            self.__email = other.__email
        else:
            self.__name = name
            self.__address = address
            self.__email = email


    def details(self):
        return f"student name : {self.__name}, student address: {self.__address}, student email: {self.__email}"

    def change_name(self, new_name):
        self.__name = new_name

# student 1
s1 = Student('pulakesh', 'hajo', 'pulakeshmalakar.official@gmail.com')
print(s1.details())

# student 2
s2 = Student(other = s1)
s2.change_name("parthib")
print(s2.details())

