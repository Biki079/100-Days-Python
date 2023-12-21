from art import logo
print(logo)
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
             's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
             's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def caeser (start_text, shift_number, cipher_direction):
    end_text = ""
    for letter in start_text:
        position = alphabets.index(letter)
        if cipher_direction == "decode":
            shift_number *= -1
        new_position = position + shift_number
        end_text += alphabets[new_position]
    print(f"The {cipher_direction} text is {end_text}.")

should_continue = True
while should_continue:
 direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
 text = input("Type your message:\n").lower()
 shift = int(input("Type the shift number: \n"))
 shift = shift % 26
 caeser(start_text=text, shift_number=shift, cipher_direction=direction)
 result = input("Type'yes' if you want to go again. Otherwise type 'no'.\n")
 if result == "no":
    should_continue = False
    print("Goodbye")