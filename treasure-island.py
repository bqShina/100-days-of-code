print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


direction = input('Which ways do you choose to go? type "Left" or "Right"? ')
lower_dir = direction.lower()
if lower_dir == "left":
  do_next = input('There is a river which has a island in the centre in front of you, do you want to swim or wait for a boat to pick you up? type "Swim" or "Wait"? \n')
  lower_next = do_next.lower()
  if lower_next == "wait":
    door = input('There are 3 doors on the house in the island, red, blue and yellow. Which door will you come in? type "Red", "Blue" or "Yellow"? \n')
    lower_door = door.lower()
    if lower_door == "red":
      print("You were burned by fire. Game Over!")
    elif lower_door == "blue":
      print("You were eaten by beasts. Game Over!")
    elif lower_door == "yellow":
      print("You Win!")
    else:
      print("Game Over.")
  else:
    print("You got attacked by trout. Game Over!")
else:
  print("You fell into a hole. Game Over!")
