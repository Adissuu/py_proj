import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


choice = int(input("What do you choose? Rock = 1, Paper = 2, Scissors = 3\n"))
match choice:
    case 1:
        print("You chose ROCK")
        print(rock)
    case 2:
        print("You chose PAPER")
        print(paper)
    case 3:
        print("You chose SCISSORS")
        print(scissors)

computer = random.randint(1, 3)

match computer:
    case 1:
        print("Computer chose ROCK")
        print(rock)
    case 2:
        print("Computer chose PAPER")
        print(paper)
    case 3:
        print("Computer chose SCISSORS")
        print(scissors)

if choice == computer:
    print("It's a draw!")
elif choice == 1 and computer == 3:
    print("You win!")
elif choice == 3 and computer == 1:
    print("You lose!")
elif computer > choice:
    print("You lose!")
elif choice > computer:
    print("You win!")
else:
    print("Reread the instructions pretty please")
