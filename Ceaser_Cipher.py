def caesar_cipher_encrypt(message, shift):
    """Encrypts a message using Caesar Cipher."""
    encrypted_message = ""
    alphabet_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    alphabet_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    for char in message:
        if char.isupper():
            index = alphabet_upper.index(char)
            new_index = (index + shift) % 26
            encrypted_message += alphabet_upper[new_index]
        elif char.islower():
            index = alphabet_lower.index(char)
            new_index = (index + shift) % 26
            encrypted_message += alphabet_lower[new_index]
        else:
            encrypted_message += char

    return encrypted_message

def caesar_cipher_decrypt(encrypted_message, shift):
    """Decrypts a message using Caesar Cipher."""
    decrypted_message = ""
    alphabet_upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    alphabet_lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    for char in encrypted_message:
        if char.isupper():
            index = alphabet_upper.index(char)
            new_index = (index - shift) % 26
            decrypted_message += alphabet_upper[new_index]
        elif char.islower():
            index = alphabet_lower.index(char)
            new_index = (index - shift) % 26
            decrypted_message += alphabet_lower[new_index]
        else:
            decrypted_message += char

    return decrypted_message

# Main program
if __name__ == "__main__":
    print("""
    ***********************************
    *     WELCOME TO CAESAR CIPHER    *
    *     Encryption & Decryption     *
    ***********************************
    """)

    action = input("Do you want to encrypt or decrypt a message? (enter 'e' or 'E' for encrypt, 'd' or 'D' for decrypt): ").strip().lower()

    if action == 'e':
        print("\n*** ENCRYPTION ***")
        message = input("Enter the message to encrypt: ")
        shift = int(input("Enter the shift value: "))
        encrypted = caesar_cipher_encrypt(message, shift)
        print("\n===================================")
        print(f"Encrypted Message: {encrypted}")
        print("===================================")
    elif action == 'd':
        print("\n*** DECRYPTION ***")
        encrypted_message = input("Enter the message to decrypt: ")
        shift = int(input("Enter the shift value used for encryption: "))
        decrypted = caesar_cipher_decrypt(encrypted_message, shift)
        print("\n===================================")
        print(f"Decrypted Message: {decrypted}")
        print("===================================")
    else:
        print("\n###################################")
        print("Invalid action. Please enter 'e' or 'E' for encrypt, 'd' or 'D' for decrypt.")
        print("###################################")
