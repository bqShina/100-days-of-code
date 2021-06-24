from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

turn_on = True
coffee_maker = CoffeeMaker()
coffee_menu = Menu()
money_machine = MoneyMachine()

while turn_on:
    options = coffee_menu.get_items()
    order = input(f"What would you like? ({options}): ").lower()
    if order == "off":
        turn_on = False
    elif order == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = coffee_menu.find_drink(order)
        coffee_can_make = coffee_maker.is_resource_sufficient(drink)        
        payment = money_machine.make_payment(drink.cost)
        if coffee_can_make and payment:
            coffee_maker.make_coffee(drink)
