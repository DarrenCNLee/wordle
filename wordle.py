#!/usr/local/bin/python3

import random

debug = False

def main():
    words = []
    wordsFile = open("words.txt", "r")
    
    while True:
        line = wordsFile.readline()
        
        if not line:
            break
        
        if len(line) == 6:
            words.append(line)
        
    wordsFile.close()
    
    solutionWord = words[random.randint(0, len(words) - 1)].rstrip().lower()
    solution = list(solutionWord)
    solLetters = set(solution)
    
    wrongGuessesLeft = 6
    
    alphabet = set("abcdefghijklmnopqrstuvwxyz")
    
    if debug:
        print(solutionWord)
    
    guessedWord = ""
    while wrongGuessesLeft > 0 and guessedWord != solutionWord:    
        guessedWord = input("Guess a word: ").lower()
        
        if len(guessedWord) != len(solution):
            print("Please enter a word with 5 letters.\n")
            print()
            continue
        
        for c in guessedWord:
            if c not in alphabet:
                print("Please enter a word with 5 letters.\n")
                print()
                continue
        
        for i in range(len(guessedWord)):
            if solutionWord[i] == guessedWord[i]:
                print(guessedWord[i] + " ", end = "")
            elif guessedWord[i] in solLetters:
                print(guessedWord[i] + "* ", end = "")
            else:
                print("_ ", end = "")
        print()
        
        wrongGuessesLeft -= 1       

            
    if guessedWord == solutionWord:
        print("Congratulations, you guessed the word correctly!")
    else:
        print("Sorry, you took too many turns.")
        print("The word was: " + solutionWord)
            
if __name__ == "__main__":
    main()