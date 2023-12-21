from art import logo
print(logo)

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
             's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
             's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_number, cipher_direction):
    end_text = ""
    for letter in start_text:
        if letter.isalpha():  # Check if the character is alphabetic
            position = alphabets.index(letter)
            if cipher_direction == "decode":
                shift_number *= -1
            new_position = (position + shift_number) % 26
            end_text += alphabets[new_position]
        else:
            end_text += letter  # Keep non-alphabetic characters unchanged
    print(f"The {cipher_direction} text is {end_text}.")

def get_user_input():
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number: \n"))
    return direction, text, shift

def main():
    should_continue = True
    while should_continue:
        direction, text, shift = get_user_input()
        shift = shift % 26  # Ensure the shift is within the alphabet range
        caesar(start_text=text, shift_number=shift, cipher_direction=direction)
        result = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n")
        if result.lower() == "no":
            should_continue = False
            print("Goodbye")

if __name__ == "__main__":
    main()
