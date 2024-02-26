from Menu import *
from CoffeeMaker import *
from MoneyMachine import *

mm = MoneyMachine()
cm = CoffeeMaker()
menu = Menu()

on = True

while on:
    options = menu.get_items()
    choice = input(f"What would you like? ({options})")
    if choice == "off":
        on = False
    elif choice == "report":
        mm.report()
        cm.report()
    else:
        drink = menu.find_drink(choice)
        if cm.is_resource_sufficient(drink) and mm.make_payment(drink.cost):
            cm.make_coffee(drink)