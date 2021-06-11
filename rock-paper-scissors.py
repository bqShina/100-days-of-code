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
choices = [rock, paper, scissors]
you_chose = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
you_chose = int(you_chose)
# 0 against 2
# 1 against 0
# 2 against 1
if you_chose >= 0 and you_chose <= 2: 
  print(choices[you_chose])
  computer_chose = random.randint(0, 2)
  print(f"Computer chose:\n{choices[computer_chose]}")
  if (you_chose == 0 and computer_chose == 2) or (you_chose == 1 and computer_chose == 0) or (you_chose == 2 and computer_chose == 1) :
    print("You win")
  elif you_chose == computer_chose:
    print("A draw")  
  else:
    print("You lose")  
else:
  print("You typed an invaild number, you lose!")
