from getpass import getpass as input

print("----------- ROCK, PAPER AND SCISSORS GAME -----------")
print()
print("\033[31m", "MAKE SURE TO USE ONLY R, P OR S", "\033[0m")
print()

score1 = 0
score2 = 0

while True:
    firstPlayer = input("Player 1: Rock, Paper or Scissors? ")
    secondPlayer = input("Player 2: Rock, Paper or Scissors? ")

    if firstPlayer == "R" or firstPlayer == "r":
        if secondPlayer == "R" or secondPlayer == "r":
            print("Two rocks rolled down the cliff, that's a tie!")
        elif secondPlayer == "P" or secondPlayer == "p":
            print("Player 2 Won, that's was easy!")
            score2 += 1
        elif secondPlayer == "S" or secondPlayer == "s":
            print("Player 1 Won, nice try Player 2!")
            score1 += 1
        else:
            print("\033[31m", "Invalid move, Player 2!", "\033[0m")
    elif firstPlayer == "P" or firstPlayer == "p":
        if secondPlayer == "P" or secondPlayer == "p":
            print("That's a tie, two papers form a book!")
        elif secondPlayer == "r" or secondPlayer == "R":
            print("Player 1 got this one!")
            score1 += 1
        elif secondPlayer == "s" or secondPlayer == "S":
            print("Player's 1 paper has been ripped apart by Player's 2 scissors!")
            score2 += 1
        else:
            print("\033[31m", "Invalid move, Player 2!", "\033[0m")
    elif firstPlayer == "S" or firstPlayer == "s":
        if secondPlayer == "S" or secondPlayer == "s":
            print("That's a tie, two scissors don't scratch each other!")
        elif secondPlayer == "R" or secondPlayer == "r":
            print("Player 2 Won, Player 1 should try harder!")
            score2 += 1
        elif secondPlayer == "P" or secondPlayer == "p":
            print("Player 1 Won, easy peasy lemon squeezy!")
            score1 += 1
    else:
        print("\033[31m", "Invalid move, Player 1!", "\033[0m")

    print("Player 1 got", score1, "points")
    print("Player 2 got", score2, "points")
    print()

    if score1 == 3 or score2 == 3:
        print("\033[31m","Good game!", "\033[0m")
        exit()
    else:
        continue