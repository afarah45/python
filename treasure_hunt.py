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
print("Your mission is to find the treasure should you choose to accept.") 

choice1 = input("Type 'left' or 'right'\n").lower()
if choice1 == "left":
  choice2 = input("You have come to a lake. Type 'wait' to wait for a boat or tpye 'swim' to swim accross\n").lower()
  if choice2 == "wait":
    choice3 = input("You arrived the thouse on the island. there are three doors, one red, one yellow and one blue. Which color do you choose?\n")
    if choice3 == "red":
      print("it is a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the the treasure! you winn")
    elif choice3 == "blue":
      print("You got eaten by beasts. Game Over")
    else:
      print("you chose door that doesn't exist\n Game Over")
  else:
    print("you got attacked by angry trout. Game Over.")
else:
    print("You fell into a whole Game Over.")