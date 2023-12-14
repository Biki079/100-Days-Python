import random
from hangman_logo import stages
from word_list import word_list

end_of_game = False

chosen_word = random.choice(word_list)

lives = 6
print(f"The solution is {chosen_word}")

display = ["_"] * len(chosen_word)

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")

    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter

    print(" ".join(display))

    if "_" not in display:
        end_of_game = True
        print("You win")

    print(stages[lives])
