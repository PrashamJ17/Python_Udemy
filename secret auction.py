from os import system # we import this to use to clear the console 
from ascii_art import sec_auc
print(sec_auc)

Bid = True
auction = {}
amt_list = []
while Bid :
    name = input("What is your name?\n")
    bid_amt = int(input("What is your bid?\n$"))
    auction[bid_amt] = name
    amt_list.append(bid_amt)
    Bidders = input("Are there any other bidders? Type 'yes or 'no'.\n").lower()
    if Bidders == 'yes':
        system('clear') # this clear the console for the bidding to be hidden
    else :
        Bid = False

winner = max(amt_list)
print(f"The winner is {auction[winner]} with a bid of ${winner}")

