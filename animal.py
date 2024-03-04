from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def make_sound(self):
        pass

    @abstractmethod
    def get_info(self):
        pass

class Tortoise(Animal):
    def __init__(self, name, age, shell_pattern):
        super().__init__(name, age)
        self.shell_pattern = shell_pattern

    def make_sound(self):
        print("hiss")

    def get_info(self):
        print(f"shell pattern: {self.shell_pattern}")
        print(f"name: {self.name}")
        print(f"age: {self.age}")

class Creep:

    tortoises = []

    def add_turtle(self, t):
        tortoises.append(t)


class Lion(Animal):

    def __init__(self, name, age, fur_color):
        super().__init__(name, age)
        self.fur_color = fur_color

    def make_sound(self):
        print("roar")

    def get_info(self):
        print(f"fur color: {self.fur_color}")
        print(f"name: {self.name}")
        print(f"age: {self.age}")


class Pride:

    lions = []

    def add_lion(self, l):
        lions.append(l)


t = Tortoise("teddy", 60, "ginger")
t.make_sound()
t.get_info()

l = Lion("ben", 30, "brown")
l.make_sound()
l.get_info()