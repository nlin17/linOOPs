class CoffeeMaker:
    def __init__(self):
        self.resources = {"water": 1000, "milk": 800, "coffee": 100}

    def report(self):
        print(f"water: {self.resources['water']}mL")
        print(f"milk: {self.resources['milk']}mL")
        print(f"coffee: {self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"There is not enough {item}")
                global can_make
                can_make = False


    def make_coffee(self, order_name):
        