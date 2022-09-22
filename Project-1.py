#!/usr/bin/env python3

"""This script will perform the game rock paper scissors"""

import random

# this function will end the game when executed


def player_attack():
    input1 = input("    ").capitalize()
    return input1


def tie():
    print("\n\n\n Black Knight: Ah foe, you think you can equal my strength?! Accept your luck. It will run out!")


def exit_game():
    print("\n\n\nOh! Had enough, eh?\nCome back and take what's coming to you, you yellow bastard!\nCome back here and take what's coming to you!\n\nI'll bite your legs off!")


def remaining_lives_block(black_knight_lives, player_shield_blocks, player):
    print(
        f"Black Knight Limbs Remaining: {black_knight_lives}\n{player}'s Shield Blocks Remaining: {player_shield_blocks}")

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


def cpu_random_attack():
    attack_choices = ("Rock", "Paper", "Scissors")
    random_attack = random.choice(attack_choices)
    return random_attack


def black_knight_dismember_print(black_knight_lives, attack, random_attack, player):

    if black_knight_lives == 3:
        black_knight_lives = print(f"\n\n\n{player} dodges the Black Knight's {random_attack}, steps aside, and cuts the Black Knight's left arm off with his {attack}. Blood spurts from the knight's open shoulder.\n\n{player}: Now stand aside, worthy adversary.\nBlack Knight: 'Tis but a scratch.\n{player}: A SCRATCH? Your arm's off!\nBlack Knight: No it isn't!\n{player}: Well what's that then? (pointing to the arm lying on the ground)\nBlack Knight: I've had worse.\n{player}: You LIAR!\nBlack Knight: Come on, you pansy!\n")
        return black_knight_lives
    elif black_knight_lives == 2:
        black_knight_lives = print(f"\n\n\n{player} dodges the armless Black Night's swift {random_attack} kick! {player} easily cuts off the black knight's right arm causing it to drop to the ground. Blood spatters freely from the stump.\n\nBlack Knight: Come on then!\n{player}: What?!?\nBlack Knight: Have at you!\n{player}: You are indeed brave, sir knight, but the fight is mine!.\nBlack Knight: Ohhh, had enough, eh?\n{player}: Look, you stupid bastard, you've got no arms left!\nBlack Knight: Yes I have!\n{player}: LOOK!!!\nBlack Knight: Just a flesh wound!")
        return black_knight_lives
    elif black_knight_lives == 1:
        black_knight_lives = print("1 lives left")
        return black_knight_lives


def player_blocks_print(blocks_left, random_attack, answer_king_queen, black_knight_lives, player_shield_blocks, player):

    if player_shield_blocks == 3 and black_knight_lives > 2:
        blocks_left = print(
            f"\nThe Black Knight dodges {player}'s strike, and hurls his {random_attack} at {player}.\n\n{player} blocks the Black Knight's {random_attack} but remains unscathed!\n\n{player}: Aha! You are as weak as I thought!\nBlack Knight: None before have passed! You will see!\n")
        return blocks_left
    elif player_shield_blocks == 3 and black_knight_lives <= 2:
        blocks_left = print(
            f"\n Surprising fast for having no arms, the Black Knight dodges {player}'s strike, and kicks his {random_attack} at {player}.\n\n{player} blocks the Black Knight's {random_attack} but remains unscathed!\n\n{player}: Aha! You are as weak as I thought!\nBlack Knight: None before have passed! I need no arms to show you that! You will see!\n")
        return blocks_left
    elif player_shield_blocks == 2 and black_knight_lives > 2:
        blocks_left = print(
            f"\n\nOnce again the Black Knight dodges {player}'s strike, and catapult's his {random_attack} at {player}.\n\n {player} barely blocks the Black Knight's {random_attack} and stumbles backwards from the blow!\n\nThat was a clsoe one sir knight! But I am a {answer_king_queen}, do you think I would be so easily conquered?\n")
    elif player_shield_blocks == 2 and black_knight_lives <= 2:
        blocks_left = print(
            f"\n\nOnce again the Black Knight dodges {player}'s strike, and super kicks his {random_attack} at {player}.\n\n {player} barely blocks the Black Knight's {random_attack} and stumbles backwards from the blow!\n\nThat was a close one sir knight! But I am a {answer_king_queen}, do you think I would be so easily conquered?\n\n Black Knight: You will soon fall to the legless Black Knight!\n")
        return blocks_left
    elif player_shield_blocks == 1 and black_knight_lives > 2:
        blocks_left = print(
            f"\n\nknight hurls {random_attack} at {player}\n")
    elif player_shield_blocks == 1 and black_knight_lives > 2:
        blocks_left = print(
            f"\n\n, the Black Knight dodges {player}'s strike, and kicks his random_attack at player knocks over {player} and destoys the {answer_king_queen}'s shield {player}: (getting up) blah blah blah\n")
        return blocks_left


def main():
    # global black_knight_lives
    # global player_shield_blocks
    # global player
    # global attack

    input1 = ""

    black_knight_lives = 4

    player_shield_blocks = 3

    while input1 != "Exit":

        print("\n\n\nWelcome to Rock, Paper, Scissors, Flesh Wound.\n\n      In this game you will be playing against the Black Knight from Monty Python and the Holy Grail.\n      The goal is to to beat the Black Knight and cross the bridge by choosing 1 of the 4 options available:\n\n\n\nRock:\n   Wins against Scissors\n   Loses against Paper.\n\nPaper:\n   Wins against Rock\n   Loses against Scissors.\n\nScissors:\n   Wins against Paper\n   Loses against Rock.\n\nFlesh Wound:\n   You'll see...\n\n\n")

        player = input("Please enter your name: ").capitalize()
        answer_king_queen = pick_king_queen()

        print(f"\n\n\nOkay {answer_king_queen} {player}, Let's go ahead and start the adventure!\n\nPlease enter:\n   '1' to grab your coconuts and gallop away!\n   'exit' to end your journey.")

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
                    f"\n\n\n'clop clop clop'\n\n'clop clop clop'\n\n'clop clop clop\n\n chhange this to the script of seeing black knight fight at bridge!\n\n\n\nBlack Knight: NONE SHALL PASS.\n\n{player}: (taken aback) What?\n\nBlack Knight: NONE SHALL PASS.\n\n{player}: I have no quarrel with you, good sir knight, but I must cross this bridge.\n\nBlack Knight: THEN YOU SHALL DIE.\n\n{player}: I *command* you, as {answer_king_queen} of the Britons, to stand aside.\n\nBlack Knight: I MOVE FOR NO {answer_king_queen.upper()}.\n\n{player}: So be it!   (draws hand and shield)")
                break
            if input1.capitalize() == "Exit":
                exit_game()
                break
            else:
                print("Please enter '1' or 'exit'.")

        while (input1 != "Exit"):
            if player_shield_blocks < 0 or black_knight_lives == 0:
                break

            print(
                "\n\n\nChoose your attack: 'Rock', 'Paper', 'Scissors', 'Flesh Wound'")
            remaining_lives_block(
                black_knight_lives, player_shield_blocks, player)

            # make a if statement to only write the battle ensues statement when limbs are 4 and blocks are 3, so it only goes once
            attack = player_attack()
            print(
                f"A battle ensues, where {player}, realitvely unencumbered by armor, has an advantage at dodging the slow heavy strikes by the Black Knight. ")
            random_attack = cpu_random_attack()

            if attack == "Rock":
                print(
                    f"\n\n\n{player} strikes the Black Knight with a very hard {attack}... the the Black Knight simultaneously strikes back with his {random_attack}")

                if random_attack == "Scissors":
                    # print black night saying oh no my arms! etc until dead
                    black_knight_lives -= 1
                    black_knight_dismember_print(
                        black_knight_lives, attack, random_attack, player)
                    # remaining_lives_block(
                    #     black_knight_lives, player_shield_blocks, player)
                elif random_attack == "Paper":
                    player_shield_blocks -= 1
                    player_blocks_print(
                        player_shield_blocks, random_attack, answer_king_queen, black_knight_lives, player_shield_blocks, player)
                    # remaining_lives_block(
                    #     black_knight_lives, player_shield_blocks, player)
                elif random_attack == "Rock":
                    tie()
                    # remaining_lives_block(
                    #     black_knight_lives, player_shield_blocks, player)

            if attack == "Paper":
                print(
                    f"\n\n\n{player} strikes the Black Knight with a very 'crinkly' attack... the the Black Knight has chosen {cpu_random_attack()}")
                if attack == "Paper" and cpu_random_attack() == "Rock":
                    print("winpaper")
                    black_knight_lives -= 1
                    print(
                        f"Black Knight Lives: {black_knight_lives}\n{player}'s Shield blocks left: {player_shield_blocks}")

                elif attack == "Paper" and cpu_random_attack() == "Scissors":
                    print("lose")
                    player_shield_blocks -= 1
                    print(
                        f"Black Knight Lives: {black_knight_lives}\n{player}'s Shield blocks left: {player_shield_blocks}")

            if attack == "Scissors":
                print(
                    f"\n\n\n{player} strikes the Black Knight with a very 'sharp' attack... the the Black Knight has chosen {cpu_random_attack()}")
                if attack == "Scissors" and cpu_random_attack() == "Paper":
                    print("winscissors")
                    black_knight_lives -= 1
                    print(
                        f"Black Knight Lives: {black_knight_lives}\n{player}'s Shield blocks left: {player_shield_blocks}")

                elif input1 == "Scissors" and cpu_random_attack() == "Rock":
                    print("lose")
                    player_shield_blocks -= 1
                    print(
                        f"Black Knight Lives: {black_knight_lives}\n{player}'s Shield blocks left: {player_shield_blocks}")
        break

        # if input1 == "Rock" and random_attack == "Scissors":
        #     print("win")
        #     break
        # elif input1 == "Rock" and random_attack == "Paper":
        #     print("lose")
        #     break
        # elif input1 == "Paper" and random_attack == "Rock":
        #     print("win")
        #     break
        # elif input1 == "Paper" and random_attack == "Scissors":
        #     print("lose")
        #     break
        # elif input1 == "Scissors" and random_attack == "Rock":
        #     print("lose")
        #     break
        # elif input1 == "Scissors" and random_attack == "Paper":
        #     print("win")
        #     break


# TODO while loops for attacks
if __name__ == "__main__":
    main()


# TODO fix the if statement so the script wont show when black knight contineus to stay at 3 lives and the p[layer goes down, only show when black knight lsoes his life!
# TODO do more parameter stuff!
# TODO use crayon.red from lab 34 to add color to the text!
# TODO add you cannot stand a chance now to armless and legless black night and wreite <pun> next to it lol
