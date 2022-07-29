import random
from hangmanpic import stages
from hangmanwords import word_list
import os

print("Welcome to hangman!")
game_is_finished = False
lives = len(stages) - 1

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

display = []
for _ in range(word_length):
    display += "_"

while not game_is_finished:
    guess = input("Guess a letter: ").lower()

    
    os.system('clear')

    if guess in display:
        print(f"You've already guessed {guess}")

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            game_is_finished = True
            print(f"The word was:{chosen_word}!")
            print("You lose.")
    
    if not "_" in display:
        game_is_finished = True
        print("You win.")

    print(stages[lives])
    
    if game_is_finished == True:
        restart = int(input("Press [1] to restart or [2] to exit to the Game Room "))
        if restart == 1:
            game_is_finished = False
            lives = len(stages) - 1

            chosen_word = random.choice(word_list)
            word_length = len(chosen_word)

            display = []
            for _ in range(word_length):
                display += "_"
        elif restart == 2:
            os.system('clear')
            os.system('python3 main.py')
