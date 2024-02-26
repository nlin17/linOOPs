class Menu:


    def __init__(self):
        self.menu = [MenuItem(name = "latte", water = 200, milk = 150, coffee = 24, cost = 2.50),
                     MenuItem(name = "cappuccino", water = 250, milk = 100, coffee = 24, cost = 3.00 ),
                     MenuItem(name = "espresso", water = 50, milk = 0, coffee = 18, cost = 1.50)]

    def find_drink(self, order_name):
        for item in self.menu:
            if item.name == order_name:
                return item
        print(f"sorry, {order_name} is not available")

    def get_items(self):
        options = ""
        for item in self.menu:
            options += f"{item.name}/"

        return options
class MenuItem:
    def __init__(self, name, water, milk, coffee, cost):
        self.name = name
        self.cost = cost
        self.ingredients = {
            "water": water,
            "milk": milk,
            "coffee": coffee
        }
