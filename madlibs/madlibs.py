# Request user inputs so they can be used on the madlib

adj = input("Adjective: ")
adj2 = input("Another adjective: ")
verb = input("Verb: ")
verb2 = input("Another verb: ")
famousPerson = input("Name a famous person: ")

#Execute the madlib with all the inputs

madlib = f"Programming is a {adj}! You can do so many {adj2} things with it. \
It makes me happy every time, because I love to {verb}. Keep coding and {verb2} like you are {famousPerson}"

#Prints the madlib

print(madlib)