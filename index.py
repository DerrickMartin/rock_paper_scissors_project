# import necessary packages , random
from random import randint

#create a list of play options 
t = ["Rock", "Paper", "Scissors"]

#Assign a random play to the computer
computer = t[randint(0,2)]

#set the player to False
player = False

while player == False:
    #set player to True
    player = input("Rock, Paper, Scissors?")
    if player == computer: 
        print("Tied!")
    elif player == "Rock":
        if computer == "paper":
            print("You lost to a computer" + computer, "Covers", player)
        else:
            print("You win!", player, "smashes", computer)
    elif player == "Paper":
        if computer == "Scissors":
            print("You lose", computer, "cuts", player)
        else:
            print("You Win!", player, "covers", computer)
    elif player == "Scissors":
        if computer == "Rock":
            print("You lose!!!", computer, "beats", player)
        else:
            print("Nice job Finally you win", player, "cuts", computer)
    else:
        print("Thats not a valid play. Check your spelling!")
    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]
        
