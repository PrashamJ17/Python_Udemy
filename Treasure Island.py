from ascii_art import treasure
print(treasure)
print("Welcome to Treasure Island !!\nYour mission is to find the treasure with the clues given!")
print("You are at cross road. Where do you want to go?")
turn = input("Type 'L' for Left or 'R' for Right\n").lower()
if turn == 'l' :
    print("You've come to a lake. There is an island in the middle of the lake.")
    lake = input("Type 'W' to'wait' to wait for a boat. Type 'S' to 'swim' across\n").lower()
    if lake == 'w':
        print("You have arrived at the island unharmed. There is a house with 3 doors.\n")
        print("One Red, one yellow and one blue. Which door would you choose ?")
        door = input("Type 'R' for Red, 'Y' for Yellow or 'B' for blue.").lower()
        if door == 'y' :
            print("You win ! Congratulations\n")
            print("******-- GAME OVER --******")
        elif door== 'r' :
            print("You were burned in Fire ! Gmae Over! Loser!")
            print("******-- GAME OVER --******")
        else :
            print("You were Eaten by beasts! Game over! Losser!")
            print("******-- GAME OVER --******")
    else :
        print("You were atttackred by a trout ! Game Over! loser!")
        print("******-- GAME OVER --******")
else :
    print("You Fall into a hole ! Game Over! lOSER")
    print("******-- GAME OVER --******")

