from ascii_art import Hangman
from random import *
print(Hangman)

lives = ['''
  +---+
  |   |
  O   |
      |
      |
      |
=========''','''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''','''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''','''  
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
word_list = ['dangal','baahubali','rrr','kgf','jawan','pk','stree','animal','bajrangi bhaijaan','dhoom','sanju','war']
chosen_word = choice(word_list)
print("Word to guess: "+'_'*len(chosen_word))

life = 6
guessed_list = []
game_over = False
while not game_over:
    guess = input("Guess a letter\n").lower()
    word=''
    for i in chosen_word:
        if i == guess:
            word += i 
            guessed_list += i
        elif i in guessed_list:
            word += i
        elif i != guess :
            word += '_'
    
    if guess not in chosen_word:
        print(f"You Guessed {guess},that's not in the word. You lose a life.")
        life -= 1
        print(lives[6-life])
        print(f"******************{life}/6 LIVES LEFT************")
        
    if guess in word :
        print(word)
        print(lives[6-life])
        print(f"******************{life}/6 LIVES LEFT************")

    if life == 1 :
        print(f"***************IT WAS {chosen_word}! YOU LOSE*****************")
        game_over = True
    if '_' not in word :
        print("**********YOU GOT IT! CONGRATS YOU WON!***********")
        game_over = True




