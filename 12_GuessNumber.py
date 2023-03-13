import random

guesses = 9
win = False
if input(
        "Welcome to the Number Guessing Game!\nI'm thinking of a number from 1 to 100.\nChoose a difficulty. Type 'easy' or 'hard': "
) != "easy":
    guesses = 6
number = random.randint(1, 100)
while guesses > 0 and not win:
    attempt = int(
        input(
            f"You have {guesses} attempt(s) remaining to guess the number.\nMake a guess: "
        ))
    if attempt == number:
        win = True
        print(f"It was {number}! Good job!")
        break
    if attempt < number:
        print("Too low.")
    elif attempt > number:
        print("Too high.")
    guesses -= 1
if guesses < 1:
    print(f"You've run out of guesses, you lost. The number was {number}")
