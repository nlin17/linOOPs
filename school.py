class Person:
    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role

    def introduce(self):
        print(f"Hi, my name is {self.name}, I am {self.age} years old, and my occupation is a {self.role}.")


class Student(Person):
    def __init__(self, name, age, major):
        super().__init__(name, age, role="Student")
        self.major = major

    def study(self):
        print(f"{self.name} is studying {self.major}")

class Teacher(Person):
    def __init__(self, name, age, subject):
        super().__init__(name, age, role = "Teacher")
        self.subject = subject

    def teach(self):
        print(f"{self.name} is teaching {self.subject}")

class Custodian(Person):
    def __init__(self, name, age, department):
        super().__init__(name, age, role = "Custodian")
        self.department = department

    def clean(self):
        print(f"{self.name} is cleaning {self.department}")


class Staff(Person):
    def __init__(self, name, age, position):
        super().__init__(name, age, role = "Staff")
        self.position = position

    def clean(self):
        print(f"{self.name} is a {self.position}")

teddy = Student("Theodorius William Buck", 44, "Dendrology")
teddy.introduce()
teddy.study()




