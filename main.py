# Nathan Gomez
# Erin Keith
# CS 333
# Final Project

from display import Display
import numpy as np
import random
import sys

def settings():
    choice = input(":")

    if(choice == 'a'):
        return "easy"

    if(choice == 'b'):
        return "medium"

    if(choice == 'c'):
        return "hard"

    if(choice == 'd'):
        return "combo"

    if(choice == 'e'):
        return "custom"

def read_file_line(file_path, line_number):
    file = open(file_path, 'r') 
  
    # read the content of the file opened 
    content = file.readlines()
    return content[line_number]

def getRandWord(difficulty):
    lines = 1
    wordLineNum = 0

    if(difficulty == "easy"):
        f = open("wordlists/easyList.txt")
        lines = len(f.readlines())
        f.close()
       
        wordLineNum = random.randint(0, lines)
        return(read_file_line("wordlists/easyList.txt", wordLineNum))

    if(difficulty == "medium"):
        f = open("wordlists/mediumList.txt")
        lines = len(f.readlines())
        f.close()
       
        wordLineNum = random.randint(0, lines)
        return(read_file_line("wordlists/mediumList.txt", wordLineNum))

    if(difficulty == "hard"):
        f = open("wordlists/hardList.txt")
        lines = len(f.readlines())
        f.close()
       
        wordLineNum = random.randint(0, lines)
        return(read_file_line("wordlists/hardList.txt", wordLineNum))

    if(difficulty == "combo"):
        f = open("wordlists/comboList.txt")
        lines = len(f.readlines())
        f.close()
       
        wordLineNum = random.randint(0, lines)
        return(read_file_line("wordlists/comboList.txt", wordLineNum))

    if(difficulty == "custom"):
        f = open("wordlists/customList.txt")
        lines = len(f.readlines())
        f.close()
       
        wordLineNum = random.randint(0, lines)
        return(read_file_line("wordlists/customList.txt", wordLineNum))

def playGame(difficulty):
    global errors
    global corrects

    errors = 0
    corrects = 0

    word = getRandWord(difficulty)
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

    if(winGame):
        Display(errors)
        print("\n")
        print("You Win!")
        corrects = 0
        words = 0
    else:
        Display(errors)
        print("\n")
        print("You Lose!")
        print("The word was: " + word)
        corrects = 0
        errors = 0

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
            difficulty = settings()
            
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
