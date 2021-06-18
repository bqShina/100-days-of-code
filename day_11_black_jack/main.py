from art import logo
import random
from replit import clear

play_game = True

def add_card(current_cards):
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card_choose = random.choice(cards)
    current_cards.append(card_choose)
    return current_cards

while play_game:
    if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == 'y':
        clear()
        print(logo)
        your_cards = []
        computer_cards = []
        add_another_card = True
        
        computer_cards = add_card(add_card(computer_cards))
        computer_score = sum(computer_cards)
        your_cards = add_card(your_cards)
        while add_another_card:
            your_cards = add_card(your_cards)
            your_score = sum(your_cards)
            if your_score > 21 and (11 in your_cards):
                for n in range(0, len(your_cards)):
                        if your_cards[n] == 11:
                            your_cards[n] = 1
                            your_score = sum(your_cards)
            print(f"    Your cards : {your_cards}, current score: {your_score}\n    Computer's first card: {computer_cards[0]}")
            if your_score > 21:                
                break                 
            choose_addcard = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if choose_addcard == "n":
                add_another_card = False
           
            while computer_score < 17 and your_score != 21:
                computer_cards = add_card(computer_cards)
                computer_score = sum(computer_cards)
        print(f"    Your final hand: {your_cards}, final score: {your_score}")
        print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}")
        # compare
        if your_score == computer_score:
            print("Draw!") 
        elif your_score == 21 or (your_score < 21 and your_score > computer_score) or (your_score < 21 and computer_score > 21):
            print("You win :)")
        else:
            print("You lose :(")

    else:
        play_game = False
