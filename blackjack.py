game_on =True
import os
def blackjackmain():
    global game_on
    global deck_list
    global deck
    import random
    import os
    print("Welcome to Blackjack!")
    print("The goal of the game is to get or get as close as you can to 21 without going over!")
    deck = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9, 10: 10, "J": 10, "Q": 10, "K": 10}
    deck_list = [1,2,3,4,5,6,7,8,9,10,"J","Q","K"]
    randomnum = random.randint(0,len(deck_list)-1)
    card_choice = deck_list[randomnum]

    def draw_a_card():
        """give a new random card everytime its called"""
        global deck
        global deck_list
        randomnum = random.randint(0,len(deck_list)-1)
        card_choice = deck_list[randomnum]
        return card_choice


    user_hand = []
    comp_hand = []

    def make_hand(hand, cards):
        """Takes the random card and puts it in your hand"""
        hand.append(cards)
        return hand

    def sum_total(hand, total):
        """takes the user/comp hand and adds the cards up in the hand to display the total"""
        global deck
        for card in hand:
            total += deck[card]
        return (total)


    user_total = 0
    comp_total = 0

    print("Heres is your starting hand:")
    make_hand(user_hand, draw_a_card())
    print(make_hand(user_hand, draw_a_card()))
    print("Here is the computers starting hand:")
    show = make_hand(comp_hand, draw_a_card())
    make_hand(comp_hand, draw_a_card())
    print(f"['XX', '{comp_hand[1]}']")

    user_total = sum_total(user_hand, user_total)
    comp_total = sum_total(comp_hand, comp_total)
    print(f"Your hand total is: {user_total}\n")

    choice = int(input("Press [1] to Hit or [2] to stay: "))

        
    if choice == 1:
        new_card = draw_a_card()
        user_hand = make_hand(user_hand, new_card)
        user_total += deck[new_card]
        #print(f"You drew a : {draw_a_card()}")
        print(f"You drew a card: {new_card}")
        print(f"Your hand total is: {user_total}")
        # choice = int(input("Press [1] to Hit or [2] to stay: "))
        if user_total == 21 or comp_total == 21:
            print("Blackjack!")
            game_on = False
        elif user_total>21 or comp_total>21:
            print("It's a Bust!")
            game_on = False
        #choice = int(input("Press [1] to Hit or [2] to stay: "))
    elif choice == 2:
        print(f"Your total: {user_total} v.s computer total: {comp_total}")
        if user_total > comp_total:
            print("You win!")
            game_on = False
        elif user_total == comp_total:
            print("It's a draw")
            game_on = False
        else:
            print("You lose")
            game_on = False
    # replay = int(input("Type [1] to play again or [2] to exit: "))
    ##os.system('clear')
    # if replay == 1:
    #     game_on = True
    #     user_hand = []
    #     comp_hand = []
    #     user_total = 0
    #     comp_total = 0

    #     print("Heres is your starting hand:")
    #     make_hand(user_hand, draw_a_card())
    #     print(make_hand(user_hand, draw_a_card()))
    #     print("Here is the computers starting hand:")
    #     show = make_hand(comp_hand, draw_a_card())
    #     make_hand(comp_hand, draw_a_card())
    #     print(f"['XX', '{comp_hand[1]}']")

    #     user_total = sum_total(user_hand, user_total)
    #     comp_total = sum_total(comp_hand, comp_total)
    #     print(f"Your hand total is: {user_total}\n")



    #     choice = int(input("Press [1] to Hit or [2] to stay: "))

        
    # else:
    #     print("Thanks for playing!")



while game_on:
    blackjackmain()
    restart = int(input("Press [1] to play again or [2] to exit to the Game Room. "))
    if restart == 2:
        print("Thanks for playing!")
        game_on = False
        os.system('clear')
        os.system('python3 main.py')
    elif restart == 1:
        os.system('clear')
        game_on = True




