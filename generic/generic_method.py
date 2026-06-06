from typing import TypeVar, Generic

F = TypeVar("F")
M = TypeVar("M")

class Employees(Generic[F,M]):
    def __init__(self):
        pass

    def print_female_employee(self, female_list:list[F]) -> list[F]:
        for female in female_list:
            print(female)

        return female_list
        
    def print_male_employee(self, male_list:list[M]) -> list[M]:
        for male in male_list:
            print(male)
        
        return male_list
    

if __name__ == "__main__":
    female = ["Sunny Leone", "Mia Khalifa", "Lisa Ann", "mia malkova", "sara jay"]
    male = ["James Deen", "Rocco Siffredi", "Manuel Ferrara", "Lexington Steele", "Brandon Iron"]

    employees: Employees[str, str] = Employees()
    
    print(employees.print_female_employee(female))

