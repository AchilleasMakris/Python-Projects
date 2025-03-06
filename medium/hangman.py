import random 
from os import sys

# get the first line if this is the one with the words words
with open("./hangman.txt", "r") as file:
    wholefile = file.read()
    words = list(map(str, wholefile.split()))
    random_word = random.choice(words)
    # print(random.choice(words))
    length = len(random_word)
    # print(length)
    print("Welcome to Hangman! Guess the hidden word by entering one letter at a time.")
    print("You have 6 chances to guess wrong before the game is over. Good luck!")
    print("Let's play Hangman! The word has been chosen. It has", length, "letters. Can you guess it?")

    print("_ _ _ _ _")

    lives = 6
    letters_found = 0
    already_guessed = 0

    guessed_letter = [0,0,0,0,0,0]
    list = [0,0,0,0,0]


    while True:    
        x = input("Guess a letter\n")
        for i in range(len(random_word)):
            if x in random_word[i]:
                letters_found += 1
                list[i] = x
                guessed_letter[i] = 1
            else:
                lives -= 1
                guessed_letter[i] = 1

        for j in range(len(list)):
            if(list[j] == 1):
                print(list[j])
            else:
                print("_ ")
                    

        if lives == 0:
            sys.exit("No lives left! The word was:", random_word)


