import random

#Setting up the game
random_word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(random_word_list)
word_length = len(chosen_word)
end_of_game = False
lives = 6
#(f'Pssst, the solution is {chosen_word}.')

#Display here is a list of "_" representing each letter in the chosen word
display = []

#Create blanks that have equal length to the chosen word
for _ in range(word_length):
    display += "_"
  
#make it possible to end the game
while not end_of_game:
    guess = input("Guess a letter: ").lower()
    #Check guessed letter, no live will be lost if the letter was already guessed
    #But a message will be displayed
    if guess in display:
        print(f"You've already guessed {guess}")


    #Here we check if the guessed letter is in a  index position in the chosen word
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            #if the letter is in the chosen word, we replace the "_" in display with the letter
            display[position] = letter
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    #Display the current state of the word
    print(f"{' '.join(display)}")
    if "_" not in display:
        end_of_game = True
        print("You win.")
    print(f"You have {lives} lives left.")