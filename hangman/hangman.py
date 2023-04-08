import random, string
from words import words

def valid_word(words):
    word = random.choice(words) #choose a random word prom the list
    while "-" in word or " " in word:
        word = random.choice(words)

    return word
    
def hangman():
    word = valid_word(words)
    word_letters = set(word) # letters in the word
    alphabet = set(string.ascii_uppercase) # list of uppercase characters in english dictionary
    used_letters = set() # user guess

    lives = 5

    # getting user input
    while len(word_letters) > 0 and lives > 0:
        # letters used
        # " ".join(["a", "b", "cd]) ---> "a b cd"
        print("You have", lives, "lives left and you used these letters: ", " ".join(used_letters))

        # what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print("Current word: ", " ".join(word_list))
    
        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives - 1 # takes a life away
                print("Letter is not in word.")

        elif user_letter in used_letters:    
            print("You already used that one, Try something new.")

        else:
            print("Invalid character! Try again.")   

    # ends here when word_letter == 0  or when lives == 0
    if lives == 0:
        print("You died. The word was", word, "better luck next time!")
    else:
        print("You guesses the word", word, "!!!")

hangman()