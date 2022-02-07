# Coffee machine program
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
Money = 0


def checker(choice):
    """Takes care of the coffee making process"""
    global Money
    water = MENU[choice]['ingredients']['water']
    coffee = MENU[choice]['ingredients']['coffee']
    milk = MENU[choice]['ingredients']['milk']
    cost = MENU[choice]['cost']
    if water <= resources['water'] and coffee <= resources['coffee'] and milk <= resources['milk']:
        paid = transaction()
        Money += round(paid, 2)
        if paid >= cost:
            resources['water'] -= water
            resources['coffee'] -= coffee
            resources['milk'] -= milk
            change = paid - cost
            change = round(change, 2)
            print(f"Here is your change ${change}.\nHere is your {choice} ☕️. Enjoy!")

    elif water > resources['water']:
        print("Sorry there is not enough water.")
    elif milk > resources['milk']:
        print("Sorry there is not enough milk.")
    else:
        print("Sorry there is not enough coffee.")


def transaction():
    """Takes care of the transactions"""
    print("Please insert coins.")
    quarter = int(input("how many quarters?: ")) * 0.25
    dimes = int(input("how many dimes?: ")) * 0.10
    nickels = int(input("how many nickles?: ")) * 0.05
    pennies = int(input("how many pennies?: ")) * 0.01
    paid = quarter + dimes + nickels + pennies
    return paid

running = True
while running:
    Choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if Choice == "off":
        running = False
    elif Choice == "report":
        print(
            f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: ${Money} ")
    elif Choice == "latte":
        checker(Choice)
    elif Choice == "espresso":
        water = MENU['espresso']['ingredients']['water']
        coffee = MENU['espresso']['ingredients']['coffee']
        cost = MENU['espresso']['cost']
        if water <= resources['water'] and coffee <= resources['coffee']:
            paid = transaction()
            Money += round(paid,2)
            if paid >= cost:
                resources['water'] -= water
                resources['coffee'] -= coffee
                change = round(paid - cost,2)
                print(f"Here is your change ${change}.\nHere is your espresso ☕️. Enjoy!")

        elif water > resources['water']:
            print("Sorry there is not enough water.")
        else:
            print("Sorry there is not enough coffee.")
    elif Choice == "cappuccino":
        checker(Choice)
    else:
        print("Wrong choice")
