import random

word_list = ["banana", "monkey", "temple", "road", "fox", "zebra", "camel", "donkey"]

chosen_word = random.choice(word_list)


print(f"The solution is {chosen_word}")

display = []
new_word = len(chosen_word)
for _ in range(new_word):
    display += "_"
print(display)
guess = input("Guess a word: ").lower()
for position in range(new_word):
    letter = chosen_word[position]
    if letter == guess:
        display[position] = letter

print(display)
    

