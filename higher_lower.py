# print the comparision a , print vs , print comparision b 
# take input from the user as to which has more followers a or b ?
# compare the data of a and b from the data file - in this first you will ha ve to import the data file . 
# extract the data of a and b , then compare the followers of and b . 
# also while printing the a and b , print their description but the not following numbers .
# if the user correctly gueeses the game continues , track the correct guesses of the user . 
# if the answer is correct then the correct answer becomes a and the new comaprision becomes b . 
# after every correct guess show the current score of the user . 
# import the random module and select the random 2 datas from the data file . 


from ascii_art import h_l,vs
from data_high_low import data
from random import *


def compare(A,B):
    if A > B :
        return 'a'
    else :
        return 'b'
    
def game():
    print(h_l)
    all_data = data
    shuffle(all_data)

    game_on = True
    n = 0
    score = 0
    data_A = all_data[n]
    while n + 1 < len(all_data) : # since the last n is the last data 
        data_B = all_data[n+1]
        print(f"Compare A: {data_A['name']}, {data_A['description']}, {data_A['country']}.")
        print(vs)
        print(f"Compare B: {data_B['name']}, {data_B['description']}, {data_B['country']}.")
        numA = data_A['follower_count']
        numB = data_B['follower_count']
        followers = input("Who has more folllowers? Type 'A' or 'B': ").lower()
        output = compare(numA,numB)
        if output == followers :
            score += 1
            print(f"You are right! Current score: {score}")
            n += 1
            if numB > numA :
                data_A = data_B
        else :
            return print(f"Sorry, that's wrong! Final score: {score}")
        
game()
