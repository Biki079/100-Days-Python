import random

stages = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

end_of_game =False
word_list = ["banana", "monkey", "temple", "road", "fox", "zebra", "camel", "donkey"]

chosen_word = random.choice(word_list)

lives = 6
print(f"The solution is {chosen_word}")

display = []
new_word = len(chosen_word)
for _ in range(new_word):
    display += "_"
print(display)
end_of_game = False
while not end_of_game:
    guess = input("Guess a word: ").lower()
    for position in range(new_word):
        letter = chosen_word[position]
        #print(f"Current Position: {position}\n Current letter: {letter}\n Correct guess: {guess}")
        if letter == guess:
            display[position] = letter
    
    if guess not in word_list:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
    print(f" ' '.join{display}")

    if _ not in display:
        end_of_game = True
        print("You win")
    
    print(stages[lives])
