import random

# Guess the number function

def guess(x):
    randomNumber = random.randint(1,x)
    guess = 0
    attempts = 1
    # The while loop checks if the user has guessed correctly
    while guess != randomNumber:
        guess = int(input(f"Guess the a number between 1 and {x} "))
        # The "if" checks if the user guessed right or if the number is too high or too low
        if guess > randomNumber:
            print("Too high! Try again.")
            attempts += 1
        elif guess < randomNumber:
            print("Too low! Try again.")
            attempts += 1
        else:
            print("That's it! The number was", randomNumber, "and it only took you", attempts, "attempts.")

# Runs the function
guess(10)
