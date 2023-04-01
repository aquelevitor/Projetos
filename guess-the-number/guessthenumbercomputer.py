import random

# Creates a function for the computer to guess a number
 
def computerGuess(x):
    low = 1
    high = x
    feedback = ""
    while feedback != "c":
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low # could be high instead, because in this case, low and high are equal.
        feedback = input(f"Is {guess} too high (h), too low (l), or it is correct (c)? ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f"The computer guessed your number {guess}, correctly!")

computerGuess(10)
             