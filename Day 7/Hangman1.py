# In this project we can create a hangman game.

import random

word_list = ["banana", "monkey", "temple", "road", "fox", "zebra", "camel", "donkey"]

chosen_word = random.choice(word_list)
guess = input("Guess a word: ").lower()

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

if guess == chosen_word:
    print("Congratulations! You guessed the word.")
else:
    print("Sorry, the correct word was:", chosen_word)

