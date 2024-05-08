def CheckWin(winGame, word, errors):
    if(winGame):
        print(word)
        print("\n")
        print("You Win!")
        return True

    elif(errors >= 7):
        print("\n")
        print("You Lose!")
        print("The word was: " + word)
        return False