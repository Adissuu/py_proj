from replit import clear
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(f"{logo}\nWelcome to the secret auction program.")
done = False
empty_dict = {}


def find_best_bidder(bid_record):
    best = 0
    winner = ""
    for bidder in bid_record:
        bid = bid_record[bidder]
        if bid > best:
            best = bid
            winner = bidder
    print(f"And the winner is... {winner}!!!")


while done == False:
    name = input("What is your name?")
    bid = int(input("What is your bid?"))
    empty_dict[name] = bid
    ongoing = input("Is there another bidder? (yes/no)")
    if ongoing != "yes":
        done = True
        clear()
        find_best_bidder(empty_dict)
    else:
        clear()
