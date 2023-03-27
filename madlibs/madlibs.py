'''Request users input to use on madlib'''

adj = input("Adjective: ")
adj2 = input("Another adjective: ")
adj3 = input("Another one: ")
adj4 = input("Last adjective: ")
noun = input("First noun: ")
noun2 = input("Second noun: ")
noun3 = input("Third noun: ")
noun4 = input("Fourth noun: ")
noun5 = input("Last noun: ")
food = input("Food name: ")
verb = input("Verb: ")
ride = input("Ride type: ")
ride2 = input("Another ride type: ")

#Execute the madlib with all the inputs

madlib = f" It was a beautiful {adj} day, and I was excited to go to the {noun} with my friends.\
We arrived early and headed straight for the {ride}. The line was so long that we decided to {verb} to pass the time.\
Finally, it was our turn to ride the {ride2}. As we were strapped in, I realized that I had left my {noun2} behind.\
I panicked, but my friend quickly pulled out a spare one from their bag. We started the ride and it was {adj3}!\
After that, we decided to grab some {food} to eat. We found a {adj4} spot to sit and enjoy our meal.\
Suddenly, we heard a loud noise and saw a {noun3} rolling towards us! We jumped up and ran out of the way just in time.\
Next, we went to play some games. My friend won a giant {noun4} and I won a small {noun5}.\
We were having so much fun that we lost track of time and realized that the park was closing.\
We rushed to the exit and took a group photo to remember our {adj3} day."


#Prints the madlib
print(madlib)
