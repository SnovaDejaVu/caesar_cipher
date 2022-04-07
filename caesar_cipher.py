from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(original_text, amount, route):
    global new_index
    new_code = ""
    for letter in original_text:
        letter_index = alphabet.index(letter)
        if route == "encode":
            new_index = letter_index + amount
        elif route == "decode":
            new_index = letter_index - amount
        new_index = new_index % 26
        new_letter = alphabet[new_index]
        new_code += new_letter
    print(f"The {route}d text is {new_code}.")


print(logo)

should_end = False
while not should_end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(original_text=text, amount=shift, route=direction)

    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        should_end = True
        print("Goodbye")

            
