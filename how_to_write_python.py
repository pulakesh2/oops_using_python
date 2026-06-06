

class Employee:
    # create the constructor
    def __init__(self, name: str, salary: int, location: str, duration: int, company: str):
        self.name = name
        self.company = company
        self.salary = salary
        self.location = location
        self.no_of_months = duration

    # get the details of the employee
    def get_details(self) -> None:
        print(f"employee name: {self.name}, he is from {self.location} and his salary per annum: {self.salary}LPA")

    # get the total salary
    def total_salary(self) -> int:
        return self.salary * self.no_of_months



if __name__ == "__main__":
    # take the details from the employees
    name: str = input("Enter your name: ")
    company: str = input("Enter your company: ")
    salary: int = int(input("Enter your salary: "))
    location: str = input("Enter your location: ")
    duration: int = int(input("how many months are you working here: "))

    # create the obj
    emp1 = Employee(name, salary, location, duration, company)

    # print those details
    emp1.get_details()
    print(f"{emp1.total_salary()}LPA")