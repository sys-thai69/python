import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_cards = []
user_cards = []
game_over = False

def deal_card():
  card = random.choice(cards)
  return card

for dealing_card in range(2):
  user_cards.append(deal_card())
  computer_cards.append(deal_card())

def calculate_score(cards):
  score_cards = cards.copy()
  if sum(score_cards) == 21 and len(score_cards) == 2:
    return 0
  if 11 in score_cards and sum(score_cards) > 21:
    score_cards.remove(11)
    score_cards.append(1)
  return sum(score_cards)

def compare(user_score, computer_score):
    if user_score > 21:
        return "You BUSTED. You lose 😭"
    if computer_score > 21:
        return "Computer busted. You WIN! 🥳"
    if user_score == computer_score:
        return "It's a PUSH (Draw) 🤝"
    if computer_score == 0: # Computer Blackjack
        return "Computer has Blackjack. You lose 😭"
    if user_score == 0: # User Blackjack
        return "You have Blackjack. You win! 🤩"
    if user_score > computer_score:
        return "You win! 🥳"
    else:
        return "You lose. 😭"

while not game_over:
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)
  print(f"Your cards: {user_cards}, current score: {user_score}")
  print(f"Computer's first card: {computer_cards[0]}")
  if user_score == 0:  #or computer_score == 0 or user_score > 21:
    print(f"U got a Blackjack!🤩 Showing computer next card...")
    print(f"Computer's cards: {computer_cards}, current score: {computer_score}")
    if computer_score == 0:
      print("Computer also has Blackjack. You draw 😭")
      game_over = True
  elif user_score > 21:
    print("You went over. You lose 😭")
    game_over = True
       
  else:
    user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
    if user_should_deal == "y":
      user_cards.append(deal_card())
    else:
      game_over = True

if computer_score != 0 and computer_score < 17 and user_score <= 21:
  print("Computer draws a card.....")
  computer_cards.append(deal_card())
  computer_score = calculate_score(computer_cards)
  
user_score = calculate_score(user_cards)
computer_score = calculate_score(computer_cards)

print(f"\n===== FINAL RESULTS =====")
print(f"Your final hand: {user_cards}, final score: {user_score}")
print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
print(compare(user_score, computer_score))



