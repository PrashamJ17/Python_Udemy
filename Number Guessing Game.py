from ascii_art import num_guess
import random

def game():
    print(num_guess)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    num = random.randint(1, 100)
    
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    life = 10 if difficulty == 'easy' else 5

    while life > 0:
        print(f"You have {life} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == num:
            print(f"You got it! The answer was {num}.")
            return
        elif guess < num:
            print("Too LOW.")
        else:
            print("Too HIGH.")

        life -= 1
        if life > 0:
            print("Guess again.\n")

    print(f"You've run out of guesses. The number was {num}. Game over.")

game()

