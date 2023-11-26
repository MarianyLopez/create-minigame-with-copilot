#-----------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See LICENSE in the project root for license information.
#-----------------------------------------------------------------------------------------
from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return app.send_static_file("index.html")

import random

def play_rock_paper_scissors():
    options = ["rock", "paper", "scissors"]
    player_score = 0

    while True:
        opponent_option = random.choice(options)

        player_option = input("Choose rock, paper, or scissors: ").lower()

        if player_option not in options:
            print("Invalid option. Please choose rock, paper, or scissors.")
            continue

        if player_option == opponent_option:
            print(f"It's a tie. Both chose {player_option}.")
        elif (
            (player_option == "rock" and opponent_option == "scissors") or
            (player_option == "scissors" and opponent_option == "paper") or
            (player_option == "paper" and opponent_option == "rock")
        ):
            print(f"You win. {player_option} beats {opponent_option}.")
            player_score += 1
        else:
            print(f"You lose. {opponent_option} beats {player_option}.")

        print(f"Current score: {player_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    play_rock_paper_scissors()
