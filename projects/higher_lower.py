print("Welcome to the Higher Lower Game!")
print(""" _   _ _       _                              _                           
| | | (_) __ _| |__   ___ _ __    ___  _ __  | |    _____      _____ _ __ 
| |_| | |/ _` | '_ \ / _ \ '__|  / _ \| '__| | |   / _ \ \ /\ / / _ \ '__|
|  _  | | (_| | | | |  __/ |    | (_) | |    | |__| (_) \ V  V /  __/ |   
|_| |_|_|\__, |_| |_|\___|_|     \___/|_|    |_____\___/ \_/\_/ \___|_|   
         |___/                                                            """)

import random

random_number = random.randint(0, 100)
print(f"Pssst, the correct answer is {random_number}")
life_line = 10
lower_bound = 0
upper_bound = 100
game_over = False


def update_life_line():
    global life_line
    life_line -= 1
    return life_line


def check_game_over():
  global game_over
  if update_life_line() == 0:
      game_over = True
      return "You've run out of guesses, you lose.\n" \
      "The correct number was {random_number}.".format(random_number=random_number)
  else:
      return "You have {life_line} guesses left.".format(life_line=life_line)


print("You have 10 attempts to guess the number between 0 and 100.")
while not game_over:
    user_guess = int(input("Make a guess: "))
    if user_guess > random_number:
        upper_bound = user_guess
        print(f"Too high. The number is between {lower_bound} and {upper_bound}.")
        print(check_game_over())
    elif user_guess < random_number:
        lower_bound = user_guess
        print(f"Too low. The number is between {lower_bound} and {upper_bound}.")
        print(check_game_over())
    else:
        print(f"You got it! The answer was {random_number}.")
        game_over = True
