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
    "bank": 0
}


def operation_attributes(type_of_coffee):
    if type_of_coffee != "espresso":
        temp_list = [MENU[type_of_coffee]["ingredients"]["water"], MENU[type_of_coffee]["ingredients"]["milk"],
                     MENU[type_of_coffee]["ingredients"]["coffee"], MENU[type_of_coffee]["cost"]]
    else:
        temp_list = [MENU[type_of_coffee]["ingredients"]["water"],
                     MENU[type_of_coffee]["ingredients"]["coffee"], MENU[type_of_coffee]["cost"]]
    return temp_list


def calculating_money(price, two, one, twenty_five, ten, order):
    good = True
    given = two * 2 + one * 1 + twenty_five * 0.25 + ten * 0.10
    back = given - price
    back = round(back, 2)
    if given < 0:
        return "You didn't put enough. Order cancelled."
    else:
        if resources["water"] >= order[0]:
            resources["water"] -= order[0]
        else:
            print("The machine doesn't have enough water, sorry.")
            good = False
        if resources["coffee"] >= order[len(order) - 2]:
            resources["coffee"] -= order[len(order) - 2]
        else:
            print("The machine doesn't have enough coffee, sorry.")
            good = False
        if order[1] > 50:
            if resources["milk"] >= order[1]:
                resources["milk"] -= order[1]
            else:
                print("The machine doesn't have enough milk, sorry.")
                good = False
        if good is True:
            resources["bank"] += price
            print(f"Thank you for ordering with us. You get {back}$ back.")


done = False
while not done:
    coffee = input(
        "What do you want to drink (Espresso, Latte, Cappuccino)").lower()
    if coffee == "espresso":
        order = operation_attributes("espresso")
    elif coffee == "latte":
        order = operation_attributes("latte")
    elif coffee == "cappuccino":
        order = operation_attributes("cappuccino")
    elif coffee == "report":
        print(resources)
        break
    else:
        print("You did not enter a valid input. Please try again.")
        break
    toonie = int(input("How many 2$ do you input?"))
    dollar = int(input("How many 1$ do you input?"))
    quarter = int(input("How many 25 cents do you input?"))
    tenth = int(input("How many ten cents do you input?"))
    calculating_money(order[len(order) - 1], toonie,
                      dollar, quarter, tenth, order)
    if input("Anything else for you good sir/lady? (yes/no): ").lower() == "no":
        done = True
