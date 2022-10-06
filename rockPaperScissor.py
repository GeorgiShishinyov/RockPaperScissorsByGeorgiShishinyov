import random
import time

games_you_want_to_play = int(input("Please enter a number of games you want to play: "))

r = "rock"
p = "paper"
s = "scissor"
computer_choose_list = [r, p, s]

for _ in range(games_you_want_to_play):
    player_choose = input("Please choose between 'rock', 'paper' and 'scissor'")
    random_computer_string = random.choice(computer_choose_list)

    print(f"You choose {player_choose}! That was nice!")
    print(f"Computer choose {random_computer_string}! Let's see who wins!... Please wait...")
    time.sleep(4)

    if player_choose == "rock" and random_computer_string == "rock":
        result = "draw"
    elif player_choose == "paper" and random_computer_string == "paper":
        result = "draw"
    elif player_choose == "scissor" and random_computer_string == "scissor":
        result = "draw"
    elif player_choose == "paper" and random_computer_string == "scissor":
        result = "lose"
    elif player_choose == "paper" and random_computer_string == "rock":
        result = "win"
    elif player_choose == "scissor" and random_computer_string == "paper":
        result = "win"
    elif player_choose == "scissor" and random_computer_string == "rock":
        result = "lose"
    elif player_choose == "rock" and random_computer_string == "paper":
        result = "lose"
    elif player_choose == "rock" and random_computer_string == "scissor":
        result = "win"

    print(result)


