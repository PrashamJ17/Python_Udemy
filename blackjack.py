from ascii_art import bj
from random import *
cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]


def game():
    play = input("Do you want to play the gameof blackjack. Type 'y' or 'n':\n").lower()
    if play =='y':
        print(bj)
        user_cards = choices(cards,k=2)
        user_sum = 0
        for i in user_cards:
            user_sum += i
        print(f"Your cards: {user_cards}, current score: {user_sum}")
        computer_cards = choices(cards,k=2)
        computer_sum = 0
        for i in computer_cards:
            computer_sum += i
        print(f"Computer's first card: {computer_cards[0]}")
        cont = True
        while cont :
            if user_sum < 21 :
                Bj = True
                while Bj:
                    hit = input("Do you want to hit or pass?\n").lower()
                    if hit == 'hit':
                        extra_user = choice(cards)
                        user_cards.append(extra_user)
                        user_sum += extra_user
                        print(f"Your cards: {user_cards}, current score: {user_sum}")
                        print(f"Computer's first card: {computer_cards[0]}")
                        if user_sum > 21 :
                            u_count = 0
                            for i in range(len(user_cards)) :
                                if user_cards[i] == 11 :
                                    u_count += 1
                            if u_count != 0 :
                                print("YOUR SCORE IS GREATER THAN 21 . CHANGING 11 TO 1")
                                user_sum = 0
                                for i in range(len(user_cards)) :
                                    if user_cards[i] == 11 :
                                        user_cards[i] = 1
                                    user_sum += user_cards[i]
                                print(f"Your cards: {user_cards}, current score: {user_sum}")
                            elif u_count == 0 :
                                Bj = False
                        elif user_sum == 21 :
                                Bj = False

                    elif hit == 'pass' :
                        Bj = False

                if user_sum > 21:
                    print(f"Computer cards: {computer_cards}, Total score: {computer_sum}")
                    return print("Burst !! You Lost !!")
                
                
                while computer_sum < 17 :
                    extra_computer = choice(cards)
                    computer_cards.append(extra_computer)
                    computer_sum += extra_computer
                    if computer_sum > 21 :
                            c_count = 0
                            for i in range(len(computer_cards)) :
                                if computer_cards[i] == 11 :
                                    c_count += 1
                            if c_count != 0 :
                                print("COMPUTER'S SCORE IS GREATER THAN 21 . CHANGING 11 TO 1")
                                computer_sum = 0
                                for i in range(len(computer_cards)) :
                                    if computer_cards[i] == 11 :
                                        computer_cards[i] = 1
                                    computer_sum += computer_cards[i]
                                print(f"Computer Final cards: {computer_cards}, Total score: {computer_sum}")
                if computer_sum > 21 :
                    print(f"Your Final cards: {user_cards}, Total score: {user_sum}")
                    print(f"Computer Final cards: {computer_cards}, Total score: {computer_sum}")
                    return print("Computer Burst ! You Won!")
                elif computer_cards == 21 :
                    print(f"Your Final cards: {user_cards}, Total score: {user_sum}")
                    print(f"Computer Final cards: {computer_cards}, Total score: {computer_sum}")
                    return ("Computer hit BlackJack ! You Lost !")
                
                print(f"Your Final cards: {user_cards}, Total score: {user_sum}")
                print(f"Computer Final cards: {computer_cards}, Total score: {computer_sum}")
                if user_sum > computer_sum :
                    return print("You Won !!")
                elif user_sum < computer_sum :
                    return print("Cmputer won! You Lost")
                else :
                    return print("Its a Draw ! Pass up")
            elif user_sum == 21 :
                return print("BlackJack!! You Win !!")
            
game()