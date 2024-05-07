# Nathan Gomez
# Erin Keith
# CS 333
# Final Project

from display import Display

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

def playGame():
	print("under construction")

def main():
	applicationRunning = True
	difficulty = "easy"
	
	while(applicationRunning):
		Display("logo")
		Display("main menu")
		choice = input(":")
				
		if(choice == 'a'):
			playGame()
			
		elif(choice == 'b'):
			Display("settings")
			difficulty = settings()
			
		elif(choice == 'c'):
			Display("tutorial")
			
		else:
			applicationRunning = False;

if __name__ == "__main__":
    main()
