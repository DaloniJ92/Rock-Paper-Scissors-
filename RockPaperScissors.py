import random
MIN = 1
MAX = 3

def main():
    playAgain = 'y'
    while playAgain == 'y':
        playChoice = int(input("Enter 1 for rock, 2 for paper or any other number for scissors "))
        if playChoice == 1:
             print("you have chosen Rock")
        elif playChoice == 2:
            print("you have chosen paper")
        else:
            print("you have chosen scissors")
        compChoice = (random.randint(MIN,MAX))
        
        if (compChoice == 1 and playChoice == 2):
            print("Paper covers scissors. You WIN!")
        elif (compChoice == 2 and playChoice == 3):
            print("Scissors cuts Paper You Win!")
        elif (compChoice == 3 and playChoice == 1):
            print ("Rock Crushes sciessors you WIN!")
        elif (compChoice == playChoice):
            print("The game is a tie.")
        else:
            print("You lost cry, yourself to sleep!")
        playAgain = (input('Enter y if you would like to play again? '))
main()
