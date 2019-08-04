# Importing library
import random

# Man body parts
man1 = ["            ___ \n", "           (o ", "o)\n", "           --", "|", "--\n", "            / ", "\ \n" ]

# Library list to store names of movies
Library=["Vikram Vedha", "Taare Zameen Par", "Andhadhun", "Bhaag Milkha Bhaag", "Jo Jeeta Wohi Sikandar", "Paan Singh Tomar", "Rang De Basanti", "Gangs of Wasseypur", "A Wednesday", "Dil Chahta Hai", "Zindagi Na Milegi Dobara", "Lage Raho Munna Bhai", "Baahubali", "Bajrangi Bhaijaan", "Gangaajal"]

# Initially zero guess
Guesses = 0
wrongGuess = []

# Choosing random movie name each time 
word = random.choice(Library).lower()
word = list(word)
n = word.__len__()
current = []

# 'j' number of letters to show to user
j = 3

# Creating hidden word for displaying to player
for i in range(n):
    if word[i] != " ":
        current.append("__")
    else:
        current.append("   ")

# Generating j ramdom indexes to show the actual letter
r=random.sample(range(0, n), j) 
for given in r:
    current[given] = word[given]


# Function display to show the current game status
def display():
    print(*man1, sep="")
    print("Wrong Guess :", *wrongGuess, sep=" ")
    print("Guesses :", Guesses)
    print("Current State :  ", end = " ")
    currentState()
    print("\n")
    print("******************************************")

# Function currentState to show the current word
def currentState():
    for i in current:
        print(i, end=" ")

# Function getData to get input letter from the user and 
# check whether the guess made by user is correct or not
def getData():
    global Guesses
    new = input()
    Guesses += 1
    flag = 1
    if new in word:
        for j in range(n):
            if word[j] == new:
                if current[j] == "__" and flag != 0:
                    current[j] = word[j]
                    flag = 0
        if flag == 1:
            wrongGuess.append(new)
            man1.__delitem__(-1)
    else:
        wrongGuess.append(new)
        man1.__delitem__(-1)

# While loop to iterate and take input from user until all the parts of man disappears
while wrongGuess.__len__() < 8 and current.count("__") != 0:
    display()
    getData()

# Finally, print winning or losing mesaage to the player
if wrongGuess.__len__() >= 8:
    print("Correct answer is ", *word, sep = " ")
    print("You Lost!!!!!")
else:
    print("You Won!!!!!!!!")
