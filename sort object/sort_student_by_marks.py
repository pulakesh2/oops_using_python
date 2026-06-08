class Student:
    def __init__(self, name, marks)->None:
        self.name = name
        self.marks = marks

    def __lt__(self, other)->bool:
        if self.marks < other.marks:
            return True
        elif self.marks > other.marks:
            return False
        else:
            return self.name < other.name
            

def sort_students(students)->list:
    students.sort()
    return students


# Example usage:
student1 = Student("Alice", 85)
student2 = Student("Bob", 75)
student3 = Student("Charlie", 85)
student4 = Student("David", 90)

students = [student1, student2, student3, student4]

sorted_students = sort_students(students)
for student in sorted_students:
    print(f"Name: {student.name}, Marks: {student.marks}")
