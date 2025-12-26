import random


number = random.randint(1, 100)
guess = None
print("Guess the number between 1 and 100\n")
while guess != number:

    try:
        guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input. Please enter a number. \n")
        continue
    if guess < number:
        print("Too low! Try again.\n")
    elif guess > number:
        print("Too high! Try again.\n")
    elif guess == number:
        print("Congratulations! You guessed the number.")
