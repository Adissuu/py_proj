choice1 = input("Welcome to treasure island!!\n You start with a choice between two roads. The left side is a dark forest, and the right side leads to a beach. (left or right)")

if choice1 == "left":
    choice2 = input(
        "You enter the forest and see a crew of pirates drinking glasses of beer. What do you do? (hide or run)")
    if choice2 == "hide":
        choice3 = input(
            "They end up leaving, and you get into a grotto where lie three doors. Which one do you open? (yellow, red, or blue)")
        if choice3 == "yellow":
            print("YOU WIN. GG")
        else:
            print("GAME OVER.")
    else:
        print("GAME OVER.")
else:
    print("GAME OVER.")
