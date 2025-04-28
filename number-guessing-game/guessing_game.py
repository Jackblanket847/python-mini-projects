import random

number = random.randint(1, 100)
attempts = 0

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100.")

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1
    if guess < number:
        print("Too low, try again!")
    elif guess > number:
        print("Too high, try again!")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
        break
