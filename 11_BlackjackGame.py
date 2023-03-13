############### Blackjack Project #####################
import random
from replit import clear
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
cards = [
    "Ace", "Ace", "Ace", "Ace", 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5,
    6, 6, 6, 6, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9, 9, 10, 10, 10, 10, "Jack",
    "Jack", "Jack", "Jack", "Queen", "Queen", "Queen", "Queen", "King", "King",
    "King", "King"
]


def count_points(list):
    sum = 0
    for element in list:
        if element == "Ace":
            element = 11
        if element == "Jack" or element == "Queen" or element == "King":
            element = 10
        sum += element
    if sum > 21 and "Ace" in list:
        sum -= 10
    return sum


# The cards in the list have equal probability of being drawn.
# The computer is the dealer.
done = False
while not done:
    card_deck = cards.copy()
    clear()
    print(logo + "\n Welcome to Blackjack! Let's start a game!")
    pick_again = True
    my_cards = []
    dealer_cards = []
    my_score = 0
    dealer_score = 0
    for i in range(2):
        my_index = random.randint(0, len(card_deck) - 1)
        my_cards.append(card_deck[my_index])
        card_deck.remove(card_deck[my_index])
        my_score = count_points(my_cards)

        dealer_index = random.randint(0, len(card_deck) - 1)
        dealer_cards.append(card_deck[dealer_index])
        card_deck.remove(card_deck[dealer_index])
        dealer_score = count_points(dealer_cards)
    print(f" Your cards: {my_cards} --> {my_score} points")
    print(f" The dealer's first card: {dealer_cards[1:]}")
    while pick_again:
        if my_score < 22 and input(
                " Enter 'y' if you wish to pick again and 'n' if you wish to stop: "
        ) == 'y':
            my_index = random.randint(0, len(card_deck) - 1)
            my_cards.append(card_deck[my_index])
            card_deck.remove(card_deck[my_index])
            my_score = count_points(my_cards)
            print(f" Your cards: {my_cards} --> {my_score} points")
        elif my_score < 22:
            pick_again = False
            while dealer_score < 17 and dealer_score < my_score:
                dealer_index = random.randint(0, len(card_deck) - 1)
                dealer_cards.append(card_deck[dealer_index])
                card_deck.remove(card_deck[dealer_index])
                dealer_score = count_points(dealer_cards)
                print(f" The dealer's cards: {dealer_cards}")
            if my_score > dealer_score or dealer_score > 21:
                print(
                    f" \n You win {my_score} to {dealer_score}! {my_cards} vs {dealer_cards}"
                )
            elif my_score == dealer_score:
                print(
                    f" \n You draw {my_score} to {dealer_score}! {my_cards} vs {dealer_cards}"
                )
            else:
                print(
                    f" \n You lose {my_score} to {dealer_score}! {my_cards} vs {dealer_cards}"
                )
        else:
            pick_again = False
            print("\n You busted!")
    if input(" \n Do you wish to play again? (y/n) ") != 'y':
        done = True
    #print(f" Your cards: {my_cards}")
    #print(f" The dealer's first card: {dealer_cards[1:]}")
