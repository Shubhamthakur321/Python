import random

choices = ["Rock", "Paper", "Scissor"]
player = False
computer = False
cpu_score = 0
player_score = 0
while True:
    computer = random.choice(choices)
    player = input("please Enter Rock, Paper, Scissor: ").capitalize()
    if player == computer:
        print("Tie")
    elif player == "Rock":
        if computer == "Paper":
            print("you loss", computer, "tear the", player)
            cpu_score = cpu_score + 1
        else:
            print("You win ", player, "break the", computer)
            player_score = player_score + 1
    elif player == "Scissor":
        if computer == "Paper":
            print("you win The game", player, "cut", computer)
            player_score = player_score + 1
        else:
            print("You loss", computer, 'break', player)
            cpu_score = cpu_score + 1

    elif player == "Paper":
        if computer == "Scissor":
            print("You loss ", computer, "cut", player)
            cpu_score = cpu_score + 1
        else:
            print("You win", player, "cut", computer)

    elif player == "End":
        print(f"Player_Score is {player_score}")
        print(f"Computer_score is {cpu_score}")
        break

