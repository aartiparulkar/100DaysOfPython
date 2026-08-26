logo = r"""
        /~~~~~~~~/|
       / /######/ / |
      / /______/ /  |
     ============ /||
     |__________|/ ||
      |\__,,__/    ||
      | __,,__     ||
      |_\====/%____||    
      | /~~~~\ %  / |
     _|/      \%_/  |
    | |        | | /
    |__\______/__|/
    ~~~~~~~~~~~~~~
"""

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def enough_coins(quarter, dime, nickel, penny):
    """Returns True if coffee can be purchased with inserted coins, False if money is insufficient."""
    inserted_money = ((0.25 * quarter) +
                      (0.10 * dime) +
                      (0.05 * nickel) +
                      (0.01 * penny))
    print(f"You inserted: ${inserted_money}")
    coffee_cost = MENU[choice]["cost"]

    if inserted_money < coffee_cost:
        print("Sorry that's not enough money. Money is refunded.")
        return -1
    else:
        return round((inserted_money - coffee_cost), 2)


def enough_resources(user_coffee):
    """Return True when order can be made, False if ingredients are insufficient."""
    for resource in user_coffee:
        if resources[resource] < user_coffee[resource]:
            print(f"Sorry, there is not enough {resource} in the machine.")
            return False
    return True


def deduct_resources(ingredients):
    for resource in ingredients:
        resources[resource] -= ingredients[resource]


print(logo)
while True:
    print("Machine functions (off/report): ")
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        break
    elif choice == "report":
        print(f"Water: {resources["water"]}")
        print(f"Milk: {resources["milk"]}")
        print(f"Coffee: {resources["coffee"]}")
    
    else:
        print("Please insert coins.")
    
        quarters = int(input("How many quarters: "))
        dimes = int(input("How many dimes: "))
        nickels = int(input("How many nickels: "))
        pennies = int(input("How many pennies: "))

        amount_left = enough_coins(quarters, dimes, nickels, pennies)
        coffee_ingredients = MENU[choice]["ingredients"]
        coffee_made = enough_resources(coffee_ingredients)

        if coffee_made:
            deduct_resources(coffee_ingredients)

            print(f"Here is ${amount_left} in change.")
            print(f"Here is your {choice}. Enjoy! ")
