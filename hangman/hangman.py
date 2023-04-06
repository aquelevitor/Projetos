import random, string
from word import words

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

    # getting user input
    user_letter = input("Guess a letter: ").upper()
    if user_letter in alphabet - used_letters:
        used_letters.add(user_letter)
        if user_letter in word_letters:
            word_letters.remove(user_letter)

    elif user_letter in used_letters:    
        print("You already used that one, Try something new.")

    else:
        print("Invalid character! Try again.")    

user_input = input("Type something: ")