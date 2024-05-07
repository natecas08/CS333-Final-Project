def Display(type):

    if(type == "logo"):
        print(" .----------------.  .----------------.  .-----------------. .----------------.  .----------------.  .----------------.  .-----------------.")
        print("| .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. || .--------------. |")
        print("| |  ____  ____  | || |      __      | || | ____  _____  | || |    ______    | || | ____    ____ | || |      __      | || | ____  _____  | |")
        print("| | |_   ||   _| | || |     /  \\     | || ||_   \\|_   _| | || |  .' ___  |   | || ||_   \\  /   _|| || |     /  \\     | || ||_   \\|_   _| | |")
        print("| |   | |__| |   | || |    / /\\ \\    | || |  |   \\ | |   | || | / .'   \\_|   | || |  |   \\/   |  | || |    / /\\ \\    | || |  |   \\ | |   | |")
        print("| |   |  __  |   | || |   / ____ \\   | || |  | |\\ \\| |   | || | | |    ____  | || |  | |\\  /| |  | || |   / ____ \\   | || |  | |\\ \\| |   | |")
        print("| |  _| |  | |_  | || | _/ /    \\ \\_ | || | _| |_\\   |_  | || | \\ `.___]  _| | || | _| |_\\/_| |_ | || | _/ /    \\ \\_ | || | _| |_\\   |_  | |")
        print("| | |____||____| | || ||____|  |____|| || ||_____|\\____| | || |  `._____.'   | || ||_____||_____|| || ||____|  |____|| || ||_____|\\____| | |")
        print("| |              | || |              | || |              | || |              | || |              | || |              | || |              | |")
        print("| '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' || '--------------' |")
        print(" '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------'  '----------------' ")

    if(type == "tutorial"):
        print("Hangman by Nathan Gomez")
        print("\n")
        print("The Game: ")
        print("Hangman is a game that tests how well you can guess a word.")
        print("You are allowed to guess one character at a time by typing ")
        print("a letter and pressing the enter key. Correct letters will ")
        print("be revealed on the word line while incorrect letters will ")
        print("be displayed on the incorrect letters row. Each incorrect ")
        print("letter that is guessed will add a segment drawn to the gallows.")
        print("If seven incorrect letters are guessed, the gallow will be ")
        print("complete and the player loses. Getting all letters correct ")
        print("wins the game. Note: all words are lowercase (except for what ")
        print("can be created by the player in the Custom difficulty) ")
        print("\n")
        print("\n")
        print("Difficulty: ")
        print("The difficulty of the game can be changed in the Settings. ")
        print("Easy: Uses only simple, short, and common words ")
        print("Medium: Uses words of average length and complexity")
        print("Hard: Uses long, complex, and rare words")
        print("Combination: Combines all of the previous lists")
        print("Custom: This allows the player to enter whatever they want as a word.")
        print("\t In order to use this, open the file labeled \"customList.txt\" within ")
        print("\t the same directory (folder) as the Hangman Executable. Enter whatever ")
        print("\t words and as many as you like into the file. No spaces can be entered ")
        print("\t and each word must be on its own seperate line.")

    if(type == "main menu"):
        print("a) Play Game")
        print("b) Settings")
        print("c) How To Play")
        print("d) Quit")

    if(type == "settings"):
        print("Difficulty: ")
        print("a) Easy")
        print("b) Medium")
        print("c) Hard")
        print("d) Combination")
        print("e) Custom")

    if(type == "0"):
        print(" _________")
        print(" |        |")
        print("          |")
        print("          |")
        print("          |")
        print("          |")
        print("      ____|__")

    if(type == "1"):
        print(" _________")
        print(" |        |")
        print(" 0        |")
        print("          |")
        print("          |")
        print("          |")
        print("      ____|__")

    if(type == "2"):
        print(" _________")
        print(" |        |")
        print(" 0        |")
        print(" |        |")
        print("          |")
        print("          |")
        print("      ____|__")

    if(type == "3"):
        print(" _________")
        print(" |        |")
        print(" 0        |")
        print("\\|        |")
        print("          |")
        print("          |")
        print("      ____|__")

    if(type == "4"):
        print(" _________")
        print(" |        |")
        print(" 0        |")
        print("\\|/       |")
        print("          |")
        print("          |")
        print("      ____|__")

    if(type == "5"):
        print(" _________")
        print(" |        |")
        print(" 0        |")
        print("\\|/       |")
        print(" |        |")
        print("          |")
        print("      ____|__")

    if(type == "6"):
        print(" _________")
        print(" |        |")
        print(" 0        |")
        print("\\|/       |")
        print(" |        |")
        print("/         |")
        print("      ____|__")

    if(type == "7"):
        print(" _________")
        print(" |        |")
        print(" 0        |")
        print("\\|/       |")
        print(" |        |")
        print("/ \\       |")
        print("      ____|__")