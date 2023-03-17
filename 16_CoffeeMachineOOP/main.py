from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
bank = MoneyMachine()

done = False
while done is False:
    query = input(f"Bonjour - Hi, What would you like? ({menu.get_items()})").lower()
    if query == "report":
        bank.report()
    else:
        item_requested = menu.find_drink(query)
        if item_requested is not None:
            if coffee_maker.is_resource_sufficient(item_requested):
                if bank.make_payment(item_requested.cost):
                    coffee_maker.make_coffee(item_requested)


