class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def printname(self):
        print(f"{self.firstName} {self.lastName}")

class Student(Person):
    def __init__(self, firstName, lastName, graduationYear):
        super().__init__(firstName, lastName)
        self.graduationYear = graduationYear
    
    def student_details(self):
        self.printname()
        print(f"Did graduate in {self.graduationYear}")

s1 = Student("Mike", "Olsen", 2020)
s1.student_details()