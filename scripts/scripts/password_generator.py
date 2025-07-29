# password_generator.py

# Generates a strong, random password using letters, numbers, and symbols

import random
import string

def generate_password(length=12):
    if length < 6:
        return "Password too short. Choose at least 6 characters."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("🔐 Random Password Generator")
try:
    user_length = int(input("Enter desired password length (min 6): "))
    print("Generated Password:", generate_password(user_length))
except ValueError:
    print("Please enter a valid number.")
