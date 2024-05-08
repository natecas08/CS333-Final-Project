import random

def read_file_line(file_path, line_number):
    file = open(file_path, 'r') 
  
    # read the content of the file opened 
    content = file.readlines()
    return content[line_number]

def GetRandWord(difficulty):
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
