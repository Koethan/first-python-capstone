import os
from motivation import motivation_quote

intro = """Welcome to the first ever edition of the game room!
This first edition comes with just single player but I am
currently thinking on how to incorporate multiplayer soon!!!\n"""

print(intro)

name = input("Please sign in so we can know what to call you:  ")
os.system('clear')
print(f"Nice to meet you, {name}!\n")
print("In the game room, you get to choose from a couple of games to play!")
print("The choices are below:")
print("----------------------------------------")
print("[1] Rock/Paper/Scissors")
print("[2] Blackjack")
print("[3] Hangman")
print("[4] Number Guessing Game")
print("[5] EXIT")
game_choice = int(input("Enter the number of the game you want to play: "))
if game_choice == 5:
    os.system('clear')
    print("Version 0.10 BETA")
    print("Thanks for playing, hope to see you soon!\n")
    print(motivation_quote)
elif game_choice == 4:
    os.system('clear')
    os.system('python3 number_guessing_game.py')
elif game_choice == 1:
    os.system('clear')
    os.system('python3 rock_paper_scissors.py')
elif game_choice == 2:
    os.system('clear')
    os.system('python3 blackjack.py')
elif game_choice == 3:
    os.system('clear')
    os.system('python3 hangman.py')
