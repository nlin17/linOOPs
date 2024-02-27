class Car:
    def __init__(self):
        self.wheels = 4
        self._color = "Black" # protected attribute--only for this class and its inherited classes
        self.__year = 2020
    def see_private(self):
        print(self.__year)



class BMW(Car):
    def __init__(self):
        print("protected attribute:", self._color)


c = Car()
print("public attribute:", c.wheels)
print("protected attribute:", c._color)
c.see_private()

