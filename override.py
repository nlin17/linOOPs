class Employee:
    def setWorkingHours(self):
        self.workingHours = 40

    def displayWorkingHours(self):
        print(self.workingHours)

class Trainee(Employee):
    def __init__(self):
        super().__init__()
    def setWorkingHours(self):
        self.workingHours = 45

    def resetWorkingHours(self):
        super().setWorkingHours()



teddy = Employee()
teddy.setWorkingHours()
teddy.displayWorkingHours()
ben = Trainee()
ben.setWorkingHours()
ben.displayWorkingHours()
ben.resetWorkingHours()
ben.displayWorkingHours()