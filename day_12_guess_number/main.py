from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
number = random.randint(1, 100)
# print(f"real number is {number}")
if level == "easy":
    attempts = 10
elif level == "hard":
    attempts = 5
guess_again = True
while guess_again:
    if attempts == 0:
        print("You've run out of guesses, you lose.")
        break
    else:
        print(f"You have {attempts} attempts remaining to guess the number.")
        guess_number = int(input("Make a guess: "))
        if guess_number > number:
            print("Too high.")
            attempts -= 1
        elif guess_number < number:
            print("Too low.")
            attempts -= 1
        else:
            print(f"You got it! The answer was {number}.")
            break
        if attempts != 0:
            print("Guess again.")

