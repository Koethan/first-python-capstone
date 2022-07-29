import random
import os
print("Welcome to the classic game of Rock Paper Scissors!\n")

computer_choice = random.randint(0,2)
user_choice = int(input("Choose [0] for Rock, [1] for Paper, or [2] for Scissors: \n"))
weapon = {0:"Rock", 1: "Paper", 2: "Scissors"}
print(f"You chose: {weapon[user_choice]} / Computer chose: {weapon[computer_choice]}")
uscore = 0
cscore = 0
game_on = True
while game_on:
    if computer_choice == user_choice:
        print("It's a draw\n")
        print(f"The score is user: {uscore} v.s. computer: {cscore}")
    elif user_choice == 0 and computer_choice == 2:
        print("You win\n")
        uscore += 1
        print(f"The score is user: {uscore} v.s. computer: {cscore}")
    elif user_choice == 0 and computer_choice == 1:
        print("You lose\n")
        cscore += 1
        print(f"The score is user: {uscore} v.s. computer: {cscore}")
    elif user_choice == 1 and computer_choice == 0:
        print("You win\n")
        uscore += 1
        print(f"The score is user: {uscore} v.s. computer: {cscore}")
    elif user_choice == 1 and computer_choice == 2:
        print("You lose\n")
        cscore += 1
        print(f"The score is user: {uscore} v.s. computer: {cscore}")
    elif user_choice == 2 and computer_choice == 1:
        print("You win\n")
        uscore += 1
        print(f"The score is user: {uscore} v.s. computer: {cscore}")
    elif user_choice == 2 and computer_choice == 0:
        print("You lose\n")
        cscore += 1
        print(f"The score is user: {uscore} v.s. computer: {cscore}\n")


    print("[1] To play again.")
    print("[2] To exit to the Game Room.")
    print("--------------------------------")
    newchoice = int(input("Wasn't that fun {name}, choose from an option above: "))
    os.system('clear')
    if newchoice == 2:
        game_on = False
        os.system('clear')
        os.system('python3 main.py')
    else:
        computer_choice = random.randint(0,2)
        user_choice = int(input("Choose [0] for Rock, [1] for Paper, or [2] for Scissors: \n"))
        print(f"You chose: {weapon[user_choice]} / Computer chose: {weapon[computer_choice]}")