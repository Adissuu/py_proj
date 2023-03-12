alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def encrypt(text, shift):
    answer = ""
    for letter in text:
        if letter not in alphabet:
            answer += letter
        else:
            x = alphabet.index(letter)
            answer += alphabet[(x + shift) % alph_len]
    print(f"Your encrypted text is {answer}.")


def decrypt(text, shift):
    answer = ""
    for letter in text:
        if letter not in alphabet:
            answer += letter
        else:
            x = alphabet.index(letter)
            answer += alphabet[(x - shift) % alph_len]
    print(f"Your decrypted text is {answer}.")


done = False
while done == False:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    alph_len = len(alphabet)

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

    if direction == "encode":
        encrypt(text, shift)
    elif direction == "decode":
        decrypt(text, shift)
    else:
        print("You didn't write a valid input for encode/decode.")
    again = input("Do you still need me? (yes, no)")
    if again != "yes":
        done = True
        print("So long, nerd.")
