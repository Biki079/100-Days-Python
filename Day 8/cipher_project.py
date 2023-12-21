alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
             's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
             's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number: \n"))

def encrypt(plain_text, shift_number):
    cipher_text = ""
    for letter in plain_text:
        if letter in alphabets:
            position = alphabets.index(letter)
            new_position = position + shift_number
            new_letter = alphabets[new_position]
            cipher_text += new_letter
        else:
            cipher_text += letter
    print(f"The encoded text is {cipher_text}")

def decrypt(cipher_text, shift_number):
    plain_text = ""
    for letter in cipher_text:
        if letter in alphabets:
            position = alphabets.index(letter)
            new_position = position - shift_number
            new_letter = alphabets[new_position]
            plain_text += new_letter
        else:
            plain_text += letter
    print(f"The decoded text is {plain_text}")

if direction == "encode":
    encrypt(plain_text=text, shift_number=shift)
elif direction == "decode":
    decrypt(cipher_text=text, shift_number=shift)
