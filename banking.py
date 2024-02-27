import random
from abc import ABCMeta, abstractmethod


class Account(metaclass=ABCMeta):
    @abstractmethod
    def createAccount(self):
        return 0


class SavingsAccount:

    def __init__(self):
        self.name = ""
        self.account = 0
        self.balance = 0
        self.records = {}

    # def __str__(self):
    #     return f"{self.records}"

    def create_account(self):
        global number
        number = random.randint(10000, 99999)
        n = input("What is your full name? ")
        d = int(input("How much are you depositing? "))
        self.name = n
        self.account = number
        self.balance = d
        self.records[number] = (n, d)
        print("Your account has been created")
        print(f"Your account number is {number} and your current balance is ${d} ")
        print(self.records)



    def authenticate(self):
        run = True
        global verification
        global n
        global num
        verification = False
        attempts = 0
        while run:
            n = input("Please enter your full name: ")
            num = int(input("Please enter your account number for verification: "))
            if n and num in self.records:
                verification = True
                run = False
                print("Verification complete")
                print(f"Welcome, {n}!")
            elif attempts == 4:
                run = False
                print("too many incorrect attempts")
            else:
                print("that is incorrect")
                attempts += 1
                print(f"Attempts remaining: {5-attempts}")


    def withdraw(self):
        withdraw_amount = int(input("How much would you like to withdraw? "))
        z = self.records[num][1]
        if z > withdraw_amount:
            self.records[num] = (n, z-withdraw_amount)
            print(f"You have successfully withdrawn ${withdraw_amount}")
            print(f"Your new balance is ${z-withdraw_amount}")
        else:
            print(f"Your balance is ${z}")
            print("You cannot withdraw that much money")

    def deposit(self):
        deposit_amount = int(input("How much would you like to deposit? "))
        z = self.records[num][1]
        self.records[num] = (n, z+deposit_amount)
        print(f"You have successfully deposited ${deposit_amount}")
        print(f"Your new balance is ${z+deposit_amount}")

    def display(self):
        b = self.records[num][1]
        print(f"Your current balance is ${b}")

s1 = SavingsAccount()


while True:
    x = int(input("What would you like to do? Press 1 to create a new account, or 2 to access an existing account: "))
    if x == 1:
        s1.create_account()

    elif x == 2:
        s1.authenticate()
        if verification == True:
            y = int(input("What would you like to do? Press 1 to withdraw, 2 to deposit, or 3 to display: "))
            if y == 1:
                s1.withdraw()

            elif y == 2:
                s1.deposit()

            elif y == 3:
                s1.display()

            else:
                print("That is not a valid option")
        else:
            print("access denied")

    else:
        print("That is not a valid option")
