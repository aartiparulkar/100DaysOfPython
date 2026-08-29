from typing import TypedDict

class Ingredients(TypedDict):
    water: int
    coffee = int
    milk = int
    
    
class MenuItem:
    """Represents a menu item.
            Args:
                name: Name of the menu item.
                cost: Cost of the menu item.
                ingredients: Ingredients required, with the amount of
                    water, coffee, and milk required.
    """
    def __init__(self, name:str, cost:float, ingredients:Ingredients):
        self.name = name
        self.cost = cost
        self.ingredients = ingredients
    

class Menu:
    """Represents a menu with drinks"""
    
    def __init__(self):
        self.menu = [
            MenuItem("espresso", 1.5, {"water": 50, "coffee": 18, "milk": 0}),
            MenuItem("latte", 2.5, {"water": 200, "coffee": 24, "milk": 150}),
            MenuItem("cappuccino", 3.0, {"water": 250, "coffee": 24, "milk": 100}),
        ]
    
    def get_items(self):
        """Returns all the names of the available menu items."""
        items = ""
        for item in self.menu:
            items += f"{item.name}/"
        return items
    
    def find_drink(self, order_name:MenuItem):
        """Searches the menu for particular drink by name. Return that item if it exists, otherwise returns None."""
        for item in self.menu:
            if item.name == order_name:
                return item
        print("Sorry that item is not available.")

