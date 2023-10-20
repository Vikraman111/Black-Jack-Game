import random
import os
from art import logo
print(logo)
print(
    "###############################################################################################Rules\n1. No jokers\n2.Ulimited deck\n3.Ace is 1 or 11\n4.Cards arent removed once drawn\n5.Value of J Q and K are 10 each\n6.Score to reach is 21\n###############################################################################################")


def card_draw(deck,own_deck):
    card = deck[random.randint(0,len(deck)-1)]
    own_deck.append(card)
def score(own_deck,score):
    for i in own_deck:
        if i in ("J","Q","K"):
            score+=10
        else:
            score+=i
    return score

def main():
    deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, "J", "Q", "K"]
    deck_len = len(deck)
    user_card = []
    user_score = 0
    comp_card = []
    comp_score = 0
    # usercard draw
    for i in range(2):
        card = deck[random.randint(0, deck_len-1)]
        user_card.append(card)
    # compcard draw
    for j in range(2):
        card = deck[random.randint(0, deck_len-1)]
        comp_card.append(card)

    print(f"Your Cards are : {user_card}")
    ch = input("Do you want to draw 1 more card? 'yes' or 'no'").lower()
    while (ch == "yes"):
        card_draw(deck, user_card)

        card_draw(deck, comp_card)
        ch = input("Do you want to draw 1 more card?").lower()

    user_score = score(user_card, user_score)
    comp_score = score(comp_card, comp_score)

    print(f"YOUR SCORE : {user_score} & COMPUTER SCORE : {comp_score}")
    if user_score < 22:
        if user_score == comp_score == 21:
            print("DRAW")
        elif user_score == 21:
            print("YOU WIN")
        elif comp_score == 21:
            print("COMPUTER WINS")
        elif user_score > comp_score:
            print("YOU WIN")
        elif user_score < comp_score:
            print("COMPUTER WINS")

    elif user_score > 21 and comp_score >21:
        print("BOTH LOST")
    elif user_score < 21 and comp_score >21:
        print("COMPUTER WINS")
    elif  user_score > 21 and comp_score < 21:
        print("COMPUTER WINS")

run = input("Do you want to play the game 'yes' or 'no'.").lower()
cnt=0
while(run == "yes"):
    main()
    run = input("Do you want to play again 'yes' or 'no'")
    os.system("cls")

print("Goodbye!")