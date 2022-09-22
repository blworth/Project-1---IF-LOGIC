#!/usr/bin/env python3

"""This script will perform the game rock paper scissors"""

import random

# this function will end the game when executed


def exit_game():
    print("\n\n\nOh! Had enough, eh?\nCome back and take what's coming to you, you yellow bastard!\nCome back here and take what's coming to you!\n\nI'll bite your legs off!")

# this function assigns king or queen to the player


def pick_king_queen():
    # global king_queen
    king_queen = ""

    while king_queen != "King" or king_queen != "Queen":
        king_queen = input(
            "Would you prefer to be a King or a Queen? ").capitalize()

        if king_queen == "King" or king_queen == "Queen":
            break
        else:
            print("Please enter 'King' or 'Queen'.")
    return king_queen


attack_choices = ("Rock", "Paper", "Scissors")

random_attack = random.choice(attack_choices)


def main():

    input1 = ""

    while input1 != "Exit":

        print("\n\n\nWelcome to Rock, Paper, Scissors, Flesh Wound.\n\n      In this game you will be playing against the Black Knight from Monty Python and the Holy Grail.\n      The goal is to to beat the Black Knight and cross the bridge by choosing 1 of the 4 options available:\n\n\n\nRock:\n   Wins against Scissors\n   Loses against Paper.\n\nPaper:\n   Wins against Rock\n   Loses against Scissors.\n\nScissors:\n   Wins against Paper\n   Loses against Rock.\n\nFlesh Wound:\n   You'll see...\n\n\n")

        player = input("Please enter your name: ").capitalize()
        answer_king_queen = pick_king_queen()

        print(f"\n\n\nOkay {player}, Let's go ahead and start the adventure!\n\nPlease enter:\n   '1' to grab your coconuts and gallop away!\n   'exit' to end your journey.")

        while (input1 != 1 or input1 != "Exit"):
            input1 = input("    ")
            input2 = ""

            if input1.isdigit():
                input2 = int(input1)
            elif input1.capitalize() == "Exit":
                exit_game()
                break
            if input2 == 1:
                print(
                    f"\n\n\n'clop clop clop'\n\n'clop clop clop'\n\n'clop clop clop\n\n Aha, it seems we have arrived!\n\n\n\nBlack Knight: NONE SHALL PASS.\n\n{player}: (taken aback) What?\n\nBlack Knight: NONE SHALL PASS.\n\n{player}: I have no quarrel with you, good sir knight, but I must cross this bridge.\n\nBlack Knight: THEN YOU SHALL DIE.\n\n{player}: I *command* you, as {answer_king_queen} of the Britons, to stand aside.\n\nBlack Knight: I MOVE FOR NO {answer_king_queen.upper()}.\n\n{player}: So be it!   (draws hands)")
                break
            if input1.capitalize() == "Exit":
                exit_game()
                break
            else:
                print("Please enter '1' or 'exit'.")

        print("\n\n\nChoose your attack: 'Rock', 'Paper', 'Scissors', 'Flesh Wound'")

        while (input1 != "Rock" or input1 != "Paper" or input1 != "Scissors" or input1 != "Flesh Wound"):
            input1 = input("    ").capitalize()
            if input1 == "Rock":
                print(
                    f"Ah, {player} very 'hardy' attack, the the Black Knight has chosen {random_attack}")
                break

            elif input1 == "Rock":
                print("test2")
                break
            elif input1 == "Rock":
                print("test3")
                break
            elif input1 == "Rock":
                print("test4")
                break
            else:
                print(
                    "\n\n\nChoose your attack: 'Rock', 'Paper', 'Scissors', 'Flesh Wound'")
                break

        break

# TODO while loops for attacks


if __name__ == "__main__":
    main()
