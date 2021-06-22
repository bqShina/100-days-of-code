from menu import MENU
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def check_resources(coffee):
    """Returns True when order can be made, False if ingredients are insufficient."""
    need_resource = MENU[coffee]["ingredients"]
    for ingredient in resources:
        if resources[ingredient] < need_resource[ingredient]:
            print(f"Sorry there is not enough {ingredient}.")
            return False
        else:
            return True


def make_coffee(coffee):
    coffee_ingredients = MENU[coffee]["ingredients"]
    coffee_cost = MENU[coffee]["cost"]
    for ingred in coffee_ingredients:
        resources[ingred] -= coffee_ingredients[ingred]
    resources["money"] += coffee_cost


machine_on = True
while machine_on:
    coffee_ordered = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if coffee_ordered == "report":
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\n")
        print(f"Coffee: {resources['coffee']}g\nMoney: ${resources['money']}\n")
    elif coffee_ordered == "off":
        machine_on = False
    else:
        sufficient = check_resources(coffee_ordered)
        if sufficient:
            quarters = int(input("Please insert coins.\nHow many quarters? "))
            dimes = int(input("How many dimes? "))
            nickles = int(input("How many nickles? "))
            pennies = int(input("How many pennies? "))
            total_coin = quarters * 0.25 + dimes * 0.10 + nickles * 0.05 + pennies * 0.01
            cost = MENU[coffee_ordered]["cost"]
            if total_coin < cost:
                print("Sorry that's not enough money. Money refunded.")
            else:
                change = total_coin - cost
                make_coffee(coffee_ordered)
                print(f"Here is ${change} in change.\nHere is your {coffee_ordered} ☕️. Enjoy!")
