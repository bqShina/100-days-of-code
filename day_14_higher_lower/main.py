import random
from game_data import data
from art import logo, vs
from replit import clear

print(logo)
score = 0
game_continue = True
a_choice = random.choice(data)
while game_continue:
    b_choice = random.choice(data)
    while a_choice == b_choice:
        b_choice = random.choice(data)
    print(f"Compare A: {a_choice['name']}, a {a_choice['description']}, from {a_choice['country']}.")
    print(vs)
    print(f"Against B: {b_choice['name']}, a {b_choice['description']}, from {b_choice['country']}.")
    answer = input("Who has more followers? Type 'A' or 'B': ").lower()
    a_followers = a_choice['follower_count']
    b_followers = b_choice['follower_count']
    clear()
    print(logo)
    if (answer == 'a' and a_followers > b_followers) or (answer == 'b' and a_followers < b_followers):
        score += 1
        a_choice = b_choice
        print(f"You're right! Current score: {score}")
    else:
        game_continue = False        
        print(f"Sorry, that's wrong. Final score: {score}")
