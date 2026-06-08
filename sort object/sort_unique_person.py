class Person:
    def __init__(self, name, age)->None:
        self.name:str = name
        self.age:int = age

    def __lt__(self,other)->bool:
        return self.name < other.name

    def __eq__(self, other):
        if not isinstance(other, Person):
            return False
        
        else:
            return self.name == other.name
        

def find_unique_persons(people)->list:
    
    unique_person : list = []

    for person in people:
        if person not in unique_person:
            unique_person.append(person)
    
    unique_person.sort()

    return unique_person
    


# Example usage:
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)
person3 = Person("Alice", 35)
person4 = Person("Charlie", 40)

people = [person1, person2, person3, person4]

unique_persons = find_unique_persons(people)
for person in unique_persons:
    print(f"Name: {person.name}, Age: {person.age}")
