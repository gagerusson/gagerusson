import random
from re import S
input("You ready to play? ")

print("""
Legal Moves-
R - Rock
P - Paper
S - Scissors""")
print("")

wins = 0
usersWins = 0
computersWins = 0
uWins = 0
cWins = 0
while True:
    rand = random.randint(1, 3)

    if rand == 1:
        computer = "R"
    elif rand == 2:
        computer = "P"
    else:
        computer = "S"

    if uWins == 3 or cWins == 3:
        if uWins > cWins:
            print("Congratulations! You beat the computer")
            usersWins += 1
        else:
            print("You lost to the computer...")
            computersWins += 1
        print("")
        play = input("Would you like to play again? Yes or No? ")
        print('')
        if play.upper() == "YES":
            uWins = 0
            cWins = 0
        else:
            break

    user = input("Make your choice: ")
    user = user.upper()
    if user == "R" or user == "P" or user == "S":

        if (user == "R" and computer == "S") or (user == "P" and computer == "R") or (user == "S" and computer == "P") :
            uWins += 1
            print(f"The computer chose {computer}, so you win that round!")
        elif user == computer:
            wins += 1
            print(f"The computer also chose {computer}, so you tie that round")
        else:
            cWins += 1
            print(f"The computer chose {computer}, so you lose that round")
    else:
        print("Please enter a valid choice!!")

    print(f"You: {uWins} Computer: {cWins}")
    print("")

print("Overall Record:")   
print(f"You: {usersWins} Computer: {computersWins}")
