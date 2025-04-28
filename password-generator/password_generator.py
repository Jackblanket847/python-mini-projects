import random
import string

print("Welcome to the Password Generator!")

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(length))

print(f"Your generated password: {password}")
