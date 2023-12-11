
import random

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
           "U", "V", "W", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "o",
           "p", "q", "r", "s", "t", "u", "w", "x", "y", "z"]

numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "@", "#", "$", "%", "*", ")", "("]

print("Welcome to password generator")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))

# Easy way:
# password = ""
# for char in range(nr_letters):
#     password += random.choice(letters)
#
# for char in range(nr_numbers):
#     password += random.choice(numbers)
#
# for char in range(nr_symbols):
#     password += random.choice(symbols)

# Hard Way:
password = []
for char in range(nr_letters):
    password.append(random.choice(letters))

for char in range(nr_numbers):
    password.append(random.choice(numbers))

for char in range(nr_symbols):
    password.append(random.choice(symbols))

random.shuffle(password)

password_str = "".join(password)
print(f"Your final password is: {password_str}")
