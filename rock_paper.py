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

#Write your code below this line 👇

images = [rock, paper, scissors]

user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_input >= 3 or user_input < 0:
  print("You selected invalid number. you lose!")
else:
  print(images[user_input])

  computer = random.randint(0,2)
  print("computer chose:")
  print(images[computer])
  
  
    
  if user_input  == 0 and computer == 2:
    
    print("your win")
    
  elif computer == 0 and user_input == 2:
    
    print("your lose")
    
  elif user_input > computer:
    print("you win")
  elif computer > user_input:
    print("you lose")
  elif user_input == computer:
    print("it's a draw!")