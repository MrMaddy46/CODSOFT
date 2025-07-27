# Password Generator using Python

import random
import string

def generate_password(length):
    if length < 4:
        return " Password too short! Use at least 4 characters."

    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

print("===== PASSWORD GENERATOR =====")

try:
    length = int(input("Enter password length (min 4): "))
    password = generate_password(length)
    print(f" Your password: {password}")
except ValueError:
    print(" Invalid input! Please enter a number.")
