logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""


def addition(first, second):
    print(f"{first} + {second} = {first+second}")
    return first + second


def substraction(first, second):
    print(f"{first} - {second} = {first-second}")
    return first - second


def multiplication(first, second):
    print(f"{first} * {second} = {first*second}")
    return first * second


def divide(first, second):
    print(f"{first} / {second} = {first/second}")
    return first / second


operations = {
    "+": addition,
    "-": substraction,
    "*": multiplication,
    "/": divide
}


def calculator():
    print(logo)

    # user enters first number
    num1 = float(input("What is your first number? "))
    for symbol in operations:
        print(symbol)
    done = False
    while not done:
        # user chooses symbol
        symbol = input("\nPick an operation from above: ")
        # user enters second number
        num2 = float(input("\nWhat is the second number? "))
        op_function = operations[symbol]
        answer = op_function(num1, num2)
        if input(
                f"\nEnter 'y' if you wish to continue using {answer} or 'n' if you wish to start again: "
        ) == "y":
            num1 = answer
        else:
            done = True
            calculator()


calculator()
