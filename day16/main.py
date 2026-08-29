from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_mc = MoneyMachine()
coffe_mc = CoffeeMaker()
menu = Menu()

choice = input(f"What would you like? \n({menu.get_items()}): ")

if choice == 'off':
    print("Turning off the coffee machine...")
elif choice == 'report_c':
    coffe_mc.report()
elif choice == "report_m":
    money_mc.report()
else:
    drink = menu.find_drink(choice)
    if drink:
        print(f"The {drink.name} is for {money_mc.CURRENCY}{drink.cost}.")        
        if coffe_mc.is_resource_sufficient(drink) and money_mc.make_payment(drink.cost):
            coffe_mc.make_coffee(drink)    
        