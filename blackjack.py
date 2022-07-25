import random
#import clear
def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  random_cards = int(random.choice(cards))
  return random_cards
#print(deal_card())
def play_game():
#11 is the Ace.
  def calculate_score(random_cards):
    """takes list of cards and calculates the score"""
    picked_cards = sum(random_cards) 
    if picked_cards == 21 and len(random_cards) == 2:
      return 0
    if 11 in random_cards and picked_cards > 21:
      random_cards.remove(11)
      random_cards.append(1)
      return sum(random_cards)  
      
    return picked_cards
    
  def compare(user_score, comp_score):
    if user_score == comp_score:
      return "Draw!"
    elif comp_score == 0:
      return "Lose, opponent has Blackjack!"
    elif user_score == 0:
      return "Win with a Blackjack"
    elif user_score > 21:
      return "You went over. You lose"
    elif comp_score > 21:
      return "Oponent went over. You win!"
    elif user_score > comp_score:
      return "You win!"
    else:
      return "You lose"
  
  user_cards = []
  computer_cards = []
  is_game_over = False
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    
  while not is_game_over:
    user_score = calculate_score(user_cards)
    comp_score = calculate_score(computer_cards)
    
    if user_score == 0 or comp_score == 0 or user_score > 21:
      is_game_over = True
    else:
      print(f"user {user_cards} total: {user_score}")
      print(f"comp {computer_cards[0]}")
      user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
      if user_should_deal == "y":
        user_cards.append(deal_card())
      else:
        is_game_over = True
  
  while comp_score != 0 and comp_score < 17:
    computer_cards.append(deal_card())
    comp_score = calculate_score(computer_cards)
    #print(f"comp {comp_score}")
    
  print(compare(user_score, comp_score))
  print(f"user final hand: {user_cards}, final score: {user_score}")
  print(f"computer final hand: {computer_cards}, final score: {comp_score}")
  
while input("Do you want play? type 'y' or 'n' ") == "y":
  #clear()
  play_game()
