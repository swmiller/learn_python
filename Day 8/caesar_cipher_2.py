from art import logo


alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


def big_banner():
    print(logo)


# Combined the encrypt and decrypt functions into a single function
# that handles both encryption and decryption based on the direction parameter.
def caesar(text, shift_amount, direction):
    result = ""
    if direction == "decode":
        shift_amount *= -1  # Reverse the shift for decryption

    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift_amount) % 26
            result += alphabet[new_position]
        else:
            result += letter  # Keep non-alphabet characters unchanged
    return result


# def ceaser_cipher(text, shift_amount, direction):
#     if direction == "encode":
#         return encrypt(text, shift_amount)
#     elif direction == "decode":
#         return decrypt(text, shift_amount)
#     else:
#         raise ValueError("Invalid direction. Use 'encode' or 'decode'.")


# def decrypt(encrypted_text, shift_amount):
#     decrypted_text = ""
#     for letter in encrypted_text:
#         if letter in alphabet:
#             position = alphabet.index(letter)
#             new_position = (position - shift_amount) % 26
#             new_letter = alphabet[new_position]
#             decrypted_text += new_letter
#         else:
#             decrypted_text += letter
#     return decrypted_text


# def encrypt(original_text, shift_amount):
#     encrypted_text = ""
#     for letter in original_text:
#         if letter in alphabet:
#             position = alphabet.index(letter)
#             new_position = (position + shift_amount) % 26
#             new_letter = alphabet[new_position]
#             encrypted_text += new_letter
#         else:
#             encrypted_text += letter
#     return encrypted_text


def get_direction():
    while True:
        direction = input(
            "\nType 'encode' to encrypt, type 'decode' to decrypt: "
        ).lower()
        if direction in ["encode", "decode"]:
            return direction
        else:
            print("\nInvalid input. Please type 'encode' or 'decode'.")


def get_text():
    while True:
        text = input("\nType your message: ").lower()
        if text.strip():
            return text
        else:
            print("\nMessage cannot be empty. Please enter a valid message.")


def get_shift():
    while True:
        try:
            shift = int(input("\nType the shift number (0-26): "))
            if 0 <= shift <= 26:
                return shift
            else:
                print("\nPlease enter a number between 0 and 26.")
        except ValueError:
            print("\nInvalid input. Please enter a valid integer.")


# direction = get_direction()
# text = get_text()
# shift = get_shift()
# result = caesar(text=text, shift_amount=shift, direction=direction)

# text_type = "encoded" if direction == "encode" else "decoded"
# print(f"\nThe resulting {text_type} text is: {result}")

# while True:
#     continue_choice = input("\nDo you want to go again? Type 'yes' or 'no': ").lower()
#     if continue_choice == "yes":
#         direction = get_direction()
#         text = get_text()
#         shift = get_shift()
#         result = caesar(text=text, shift_amount=shift, direction=direction)
#         text_type = "encoded" if direction == "encode" else "decoded"
#         print(f"\nThe resulting {text_type} text is: {result}")
#     elif continue_choice == "no":
#         print("\nGoodbye!")
#         break
#     else:
#         print("\nInvalid input. Please type 'yes' or 'no'.")


# ...existing code...

if __name__ == "__main__":
    big_banner()
    print("Welcome to the Caesar Cipher program!")

    direction = get_direction()
    text = get_text()
    shift = get_shift()
    result = caesar(text=text, shift_amount=shift, direction=direction)

    text_type = "encoded" if direction == "encode" else "decoded"
    print(f"\nThe resulting {text_type} text is: {result}")

    while True:
        continue_choice = input(
            "\nDo you want to go again? Type 'yes' or 'no': "
        ).lower()
        if continue_choice == "yes":
            direction = get_direction()
            text = get_text()
            shift = get_shift()
            result = caesar(text=text, shift_amount=shift, direction=direction)
            text_type = "encoded" if direction == "encode" else "decoded"
            print(f"\nThe resulting {text_type} text is: {result}")
        elif continue_choice == "no":
            print("\nGoodbye!")
            break
        else:
            print("\nInvalid input. Please type 'yes' or 'no'.")
