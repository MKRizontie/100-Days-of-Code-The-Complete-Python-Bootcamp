import random

print("Welcome to the Password Generator!")

# Input: Number of alphabets, digits, and symbols
num_alphabets = int(input("Enter the number of alphabets: "))
num_digits = int(input("Enter the number of digits: "))
num_symbols = int(input("Enter the number of symbols: "))

# Validate inputs
total_length = num_alphabets + num_digits + num_symbols

# Lists of characters
alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
             'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']  # Contains digits 0-9
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+', '[', ']', '{', '}', '|', ';', ':', '\'', ',', '.', '<', '>', '/', '?', '`']  # Contains special characters

# Generate password components
password = []

for _ in range(num_alphabets):
    password.append(random.choice(alphabets))

for _ in range(num_digits):
    password.append(random.choice(digits))

for _ in range(num_symbols):
    password.append(random.choice(symbols))

# Shuffle the password to ensure randomness
random.shuffle(password)

# Convert list to string
final_password = "".join(password)

print(f"Your generated password is: {final_password}")
