import random
import os
#from main import name

print(f"Welcome to the number guessing game!")
print("Try to guess a number for 1 to 100 with a limited amount of lives!\n")


# def game_function(lives):
#     global easy, hard
#     answer = random.randint(1, 100)
#     guess = int(input("Please guess a number: "))
#     if guess == answer:
#         print("You got it right!!!")
#     elif guess < answer:
#         print("Your guess is too small")
#         lives -= 1
#         return lives
#     elif guess > answer:
#         lives -= 1
#         return lives
#         print("Your guess is too high")



easy = 10
hard = 5
answer = random.randint(1,100)
print(answer)
print("DIFFICULTY LEVELS")
print("---------------------")
print("[1] Easy = 10 lives")
print("[2] Hard = 5 lives")
difficulty = int((input("Choose the difficulty you want to try: ")))
lives = 0
if difficulty == 1:
    lives = 10
else:
    lives = 5
##I need to find a way make the game restart 
keep_going = True
while keep_going:
    game_on = True
    while game_on:
        
        if difficulty == 1:
            print(f"You have {lives} lives left:")
            guess = int(input("Please guess a number: "))  
            if guess == answer:
                print("You got it right!!!")
                break
            elif guess < answer:
                print("Your guess is too small")
                lives -= 1
            elif guess > answer:
                lives -= 1
                print("Your guess is too high")
        elif difficulty == 2:
            print(f"You have {lives} lives left")
            guess = int(input("Please guess a number: "))
            if guess == answer:
                print("You got it right!!!")
                break
            elif guess < answer:
                print("Your guess is too small")
                lives -= 1
            elif guess > answer:
                lives -= 1
                print("Your guess is too high")
        else:
            print("Please choose an available option!")
            break
        if lives == 0:
            break

    os.system('clear')
    print(f"Game's over, the answer was {answer}\n")
    print("[1] To play again.")
    print("[2] To exit to the Game Room.")
    print("--------------------------------")
    newchoice = int(input("Wasn't that fun {name}, choose from an option above: "))
    if newchoice == 2:
        keep_going = False
        os.system('clear')
        os.system('python3 main.py')
