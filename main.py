# Nathan Gomez
# Erin Keith
# CS 333
# Final Project

from display import Display
from checkWin import CheckWin
from getRandWord import GetRandWord
from settings import Settings

import numpy as np
import sys


def playGame(difficulty):
    global errors
    global corrects

    errors = 0
    corrects = 0

    word = GetRandWord(difficulty)
    word = word[:-1]
    
    truthArray = np.array([False]*len(word))
    winGame = False
    wrongChars = np.array([' ']*26)
    wrongInt = 0

    while(errors < 7 and not winGame):
        errorFlag = True
        displayError = chr(errors + 48)
        Display(displayError)
        print("\n")

        counter = 0
        for i in word:
            if(truthArray[counter] == False):
                sys.stdout.write("_");
            else:
                sys.stdout.write(i)
            counter += 1
        print("\n")

        print("Wrong Guesses: ")
        for i in wrongChars:
            sys.stdout.write(i)
        print("\n")

        counter = 0
        guess = input("guess: ")
        for i in word:
            correctCharRepeat = False;
            if(guess == i):
                if(truthArray[counter] == False):
                    corrects += 1
                    truthArray[counter] = True
                    errorFlag = False
            counter += 1

        repeatLetter = False
        counter = 0
        if(errorFlag == True):
            errors += 1
            for i in truthArray:
                if(guess == wrongChars[counter]):
                    repeatLetter = True
                counter += 1
            if(repeatLetter == False):
                wrongChars[wrongInt] = guess
                repeatLetter = False
            else:
                repeatLetter = False
            wrongInt += 1

        if(corrects >= len(word)):
            winGame = True

        win = CheckWin(winGame, word, errors)
        

def main():
    applicationRunning = True
    difficulty = "easy"

    while(applicationRunning):
        Display("logo")
        print("Game Mode: " + difficulty)
        print("\n")
        Display("main menu")
        
        choice = input(":")

        if(choice == 'a'):
            playGame(difficulty)

        elif(choice == 'b'):
            print("\n\n")
            Display("settings")
            choice = input(":")
            difficulty = Settings(choice)
            
        elif(choice == 'c'):
            print("\n\n")
            Display("tutorial")

        elif(choice == 'd'):
            applicationRunning = False;

        else:
            print("\n\n")
            print(choice + " was not a valid option")
        print("\n\n")

if __name__ == "__main__":
    main()
