def computer_play():
#   while calculate_score(computer_cards) != 0 and calculate_score(computer_cards) < 17:
#     computer_cards.append(deal_card())

# while not game_over:
#   user_score = calculate_score(user_cards)
#   computer_score = calculate_score(computer_cards)
#   print(f"Your cards: {user_cards}, current score: {user_score}")
#   print(f"Computer's first card: {computer_cards[0]}")
#   if user_score == 0 or computer_score == 0 or user_score > 21:
#     game_over = True
#   elif user_score < 21:
#     user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
#     if user_should_deal == "y":
#       user_cards.append(deal_card())
#       user_score = calculate_score(user_cards)
#       print(f"Your cards: {user_cards}, current score: {user_score}")
#       print(f"Computer's card: {computer_cards}")
#       computer_play()
#   else:
#     print(f"Your final hand: {user_cards}, final score: {user_score}")
#     print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
#     game_over = True