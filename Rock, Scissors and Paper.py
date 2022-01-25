# Rock, Scissors & Paper Game

#Importing the library
import random

#Setting up the list of rock, scissors and paper
options = ['rock', 'scissors', 'paper']

#Score set to 0 for both player and the computer
user_score = 0
computer_score = 0

#Randomising the computer's choice
computer_choice = random.randint(0, 2)

#Showing the process
while True:
    to_play = int(input("Choose Rock [0], Scissors [1] or Paper [2]. [3] to end the game. "))
    if to_play == 3:
        print(f"Your score is {user_score}.")
        print(f"The computer score is {user_score}.")
        print("Goodbye.")
        quit()
    if to_play not in [0, 1, 2, 3]:
        print("Try a correct number")
    else:
        if to_play == 0 and computer_choice == 1 or to_play == 1 and computer_choice == 2 or to_play == 2 and computer_choice == 0:
            user_score += 1
            print("You chose", options[to_play], "and the computer chose", options[computer_choice], ". You win.")
        elif to_play == computer_choice:
            print("You chose", options[to_play], "and the computer chose", options[computer_choice], ". You both draw.")
        else:
            computer_score += 1
            print("You chose", options[to_play], "and the computer chose", options[computer_choice], ". The computer wins.")

