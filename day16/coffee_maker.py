from typing import TypedDict
from menu import MenuItem

class Resources(TypedDict):
    water: int
    coffee: int
    milk: int
    
    
class CoffeeMaker:
    UNITS = {
        "water": "ml",
        "milk": "ml",
        "coffee": "g"
    }
    
    def __init__(self):
        self.resources: Resources = {
            "water": 300, 
            "coffee": 100, 
            "milk": 200
        }

    def report(self):
        """Prints the current ingredients left in the machine."""
        for res, amt in self.resources.items():
            print(f"{res.capitalize()}: {amt}{self.UNITS[res]}")
            
    def is_resource_sufficient(self, drink: MenuItem):
        """Returns True if the coffee machine has enough ingredients to make the specified drink, False otherwise."""
        for ingredient in drink.ingredients:
            if self.resources[ingredient] <= drink.ingredients[ingredient]:
                print(f"Sorry there is not enough {ingredient}")
                return False
        return True
    
    def make_coffee(self, order_name: MenuItem):
        """Deducts the required ingredients from the resources."""
        for ingredient in order_name.ingredients:
            self.resources[ingredient] -= order_name.ingredients[ingredient]
        print(f"Here is your {order_name.name}. Enjoy!")
        return self.resources
    