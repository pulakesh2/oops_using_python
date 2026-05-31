class Animal:
    def __init__(self, breed_name):
        self.breed_name = breed_name

    def bark(self):
        return f"{self.breed_name} barked"


# inherit class
class Dog(Animal):
    def __init__(self, breed_name,nick_name):
        # inherit info
        super().__init__(breed_name)
        self.nick_name = nick_name

    #
    def details(self):
        return f"breed name : {self.breed_name}, nick name : {self.nick_name}"


golden_retriever = Animal("Golden Retriever")
dog = Dog("Golden Retriever","dog")



print(golden_retriever.bark())

print(dog.details())
