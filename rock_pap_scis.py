#Rock paper scissors game with replayability
import random

#defines win conditions
def win_conditions(user, comp):
    if (user == 'r' and comp == 's') \
      or (user == 's' and comp == 'p') \
      or (user == 'p' and comp == 'r'):
        return True

#defines and returns results of the game
def outcomes(user, comp):
    if win_conditions(user, comp):
        return 'You Win!'
    if user == comp:
        return 'Draw!'
    return 'You Lose!'

#Main game loop
def play():
    while True:
        #ask for user input
        user = input("What do you choose? 'r' for rock, 'p' for paper, 's' for scissor: ").lower()

        #validate users input
        if user not in ['r', 'p', 's']:
            print("Invalid choice. Please choose either 'r', 'p', or 's'.")
            continue

        #generate computers choice
        comp = random.choice(['r','p','s'])

        #store as dict for readability
        choice = {'r': 'Rock', 'p': 'Paper', 's': 'Scissors'}

        #display comp choice
        print(f"You chose: {choice[user]}")
        print(f"Computer chose: {choice[comp]}")

        #print results
        result = outcomes(user, comp)
        print(result)

        #ask if the user wants to play again
        while True:
            replay = input("Do you want to play again? (y/n): ").lower() #incase user uses capitals
            if replay == 'y':
                break
            elif replay == 'n':
                print("Thanks for playing!")
                return
            else:
                print("Please choose 'y' to play again or 'n' to quit")

play()






