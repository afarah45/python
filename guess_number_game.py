import random
easy_level = 10
hard_level = 5
#takes input from user and sets level
def set_difficulty():
  level = input("choose a difficulty level. Type easy or hard ")
  if level == "easy":
    return easy_level
  else:
    return hard_level 

def game():
#checks the user answer agains the computer gerated answer.
  def check_answer(guess_number, random_number, turns):
    """checks the answer agains the random"""
    if guess_number > random_number:
      print("Too high.")
      return turns -1
    elif guess_number < random_number:
      print("Too low")
      return turns -1
    else:
      print(f"You got it, the correct is {random_number}")
  #welcome the user and create random range of numbers    
  print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100. ")
  random_number = random.randint(1, 100)
  print(f"Pssst the correct number is {random_number} ")
  turns = set_difficulty()
  
  #allows the user to contue to guess and till run out of attempts
  guess_number = 0
  while guess_number != random_number:
    print(f"You have {turns} attempts remaining to guess the number")
    guess_number = int(input("Make a guess "))
    turns = check_answer(guess_number, random_number, turns)
    if turns == 0:
      print("you've run out of guesses, you lose")
      return 
game()


  
