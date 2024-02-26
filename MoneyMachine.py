class MoneyMachine:
    currency = "$"
    coin_values = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickels": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        print(f"Money: {self.currency}{self.profit}")

    def process_coins(self):
        print("please insert coins")
        for coin in self.coin_values:
            self.money_received += int(input(f"how many {coin}? ")) * self.coin_values[coin]
        return self.money_received

    def make_payment(self, cost):
        # return true when payment is accepted, false if insufficient
        self.process_coins()
        if self.money_received >= cost:
            print("payment successful")
        else:
            print("That is not enough money")
