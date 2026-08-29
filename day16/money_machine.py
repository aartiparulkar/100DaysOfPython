class MoneyMachine:
    CURRENCY = "$"
    COINS = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }
    
    def __init__(self):
        self.money_recieved = 0
        self.profit = 0
    
    def report(self):
        """Prints the current profit"""
        print(f"Today's Earnings: {self.CURRENCY}{self.money}")
    
    def process_coins(self):
        """Returns the total amount from coins inserted."""
        print("Please enter coins.")
        for coin in self.COINS:
            self.money_recieved += int(input(f"How many {coin}?: ")) * self.COINS[coin]
        return self.money_recieved
        
    def make_payment(self, cost):
        """Returns True when payment is accepted and False otherwise."""
        self.process_coins()
        if self.money_recieved >= cost:
            change = self.money_recieved - cost
            print(f"Here's your ${round(change, 2)}.")
            self.profit += cost
            self.money_recieved = 0
            return True
        print("Sorry, that's not enough money. Money Refunded.")
        return False
    