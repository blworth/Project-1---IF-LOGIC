#!/usr/bin/env python3

"""This script will perform the game rock paper scissors"""

import random

import crayons


# this function will end the game when executed


def player_attack(player_shield_blocks, black_knight_lives, player, Y):
    input1 = input("    ").capitalize()

    if player_shield_blocks == 3 and black_knight_lives == 4:
        print(
            f"\n\n\n{Y(f'A battle ensues, where {player}')}{Y(', realitvely unencumbered by armor, has an advantage at dodging the slow heavy strikes by the Black Knight.')}")
    return input1


def tie(Y, knight):
    print(f"\n\n\n{knight}{Y(': Ah foe, you think you can equal my strength?! Accept your luck. It will run out!')}")


def exit_game(Y, punc):
    print(f"\n\n\n{Y('Oh! Had enough, eh?')}\n{Y(f'Come back and take what{punc}s coming to you, you yellow bastard!')}\n{Y(f'Come back here and take what{punc}s coming to you!')}\n\n{Y(f'I{punc}ll bite your legs off!')}")


def remaining_lives_block(black_knight_lives, player_shield_blocks, player, knight, Y, punc):
    print(
        f"{Y(f'{knight}')} {Y(f'Limbs Remaining: {black_knight_lives}')}\n{Y(f'{player}')}{Y(f'{punc}s Shield Blocks Remaining: ')}{Y(f'{player_shield_blocks}')}")

# this function assigns king or queen to the player


def pick_name(Y):
    # global king_queen
    print(f"{Y('Please enter your name: ')}")
    name = input("    ").capitalize()
    return crayons.cyan(name)


def pick_king_queen(Y, punc, R):
    # global king_queen
    king_queen = ""
    king = crayons.cyan("King")
    queen = crayons.cyan("Queen")

    while king_queen != "King" or king_queen != "Queen":
        print(f"{Y(f'Would you prefer to be a {king}')} {Y(f'or a {queen}')}{Y('? ')}")
        king_queen = input("    ").capitalize()

        if king_queen == "King" or king_queen == "Queen":
            break
        else:
            print(
                f"{R(f'Please enter {punc}{king}')}{R(f'{punc} or {punc}')}{R(f'{queen}')}{R(f'{punc}.')}\n")
    return crayons.cyan(king_queen)


def cpu_random_attack(rock, paper, scissors):
    attack_choices = ((f"{rock}"), (f"{paper}"), (f"{scissors}"))
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
    rock = crayons.blue('Rock')
    paper = crayons.green('Paper')
    scissors = crayons.black('Scissors')
    flesh = crayons.red('Flesh Wound')
    Y = crayons.yellow
    R = crayons.red
    # fix all the stud make rock be rock not R and etc make yellow be yellow not Y
    # knight be knight not b
    # TODO also change and where there is queen or king to the cyan and anywhere you see knight to the knight magenta
    knight = crayons.magenta('Black Knight')
    you = crayons.cyan('you')
    one = crayons.cyan('1')
    Exit = crayons.cyan('Exit')
    punc = "'"

    black_knight_lives = 4

    player_shield_blocks = 3

    while input1 != "Exit":

        print(f"\n\n{crayons.yellow('Welcome to')} {rock}, {paper}, {scissors}, {flesh}.\n\n      {crayons.yellow(f'In this game {you}')} {Y(f'will be playing against the {knight}')} {Y('from Monty Python and the Holy Grail.')}\n      {crayons.yellow(f'The goal is to to beat the {knight}')} {Y('and cross the bridge by choosing 1 of the 4 options available:')}\n\n{rock}{Y(':')}\n   {Y('Wins against')} {scissors}\n   {Y('Loses against')} {paper}\n\n{paper}{Y(':')}\n   {Y('Wins against')} {rock}\n   {Y('Loses against')} {scissors}\n\n{scissors}{Y(':')}\n   {Y('Wins against')} {paper}\n   {Y('Loses against')} {rock}\n\n{flesh}{Y(':')}\n   {Y('You will see...')}\n\n\n")

        player = pick_name(Y)
        answer_king_queen = pick_king_queen(Y, punc, R)

        print(f"\n\n\n{Y('Okay')} {answer_king_queen} {player}{Y(f', Let{punc}s go ahead and start the adventure!')}\n\n{Y('Please enter:')}\n   {Y(f'{punc}{one}')}{Y(f'{punc} to grab your coconuts and gallop away!')}\n   {Y(f'{punc}{Exit}')}{Y(f'{punc} to end your journey.')}")

        while (input1 != 1 or input1 != "Exit"):
            input1 = input("    ")
            input2 = ""

            if input1.isdigit():
                input2 = int(input1)
            elif input1.capitalize() == "Exit":
                exit_game(Y, punc)
                quit()
            if input2 == 1:
                print(
                    f"\n\n\n{Y('<clop clop clop>')}\n\n{Y('<clop clop clop>')}\n\n{Y('<clop clop clop>')}\n\n{Y('chhange this to the script of seeing black knight fight at bridge!')}\n\n\n\n{Y(f'{knight}')}{Y(': NONE SHALL PASS.')}\n\n{Y(f'{player}')}{Y(': (taken aback) What?')}\n\n{Y(f'{knight}')}{Y(': NONE SHALL PASS.')}\n\n{Y(f'{player}')}{Y(': I have no quarrel with you, good sir knight, but I must cross this bridge.')}\n\n{Y(f'{knight}')}{Y(': THEN YOU SHALL DIE.')}\n\n{Y(f'{player}')}{Y(f': I *command* you, as {answer_king_queen}')}{Y(' of the Britons, to stand aside.')}\n\n{Y(f'{knight}')}{Y(f': I MOVE FOR NO {answer_king_queen.upper()}')}{Y('.')}\n\n{Y(f'{player}')}{Y(': So be it!   (draws hand and shield)')}")
                break
            else:
                print(
                    f"{R(f'Please enter {punc}{one}')}{R(f'{punc} or {punc}{Exit}')}{R(f'{punc}.')}")

        while (input1 != "Exit"):
            if player_shield_blocks < 0 or black_knight_lives == 0:
                break

            print(
                f"\n\n\n{Y('Choose your attack: ')}{Y(f'{rock}')}{Y(',')} {Y(f'{paper}')}{Y(',')} {Y(f'{scissors}')}{Y(',')} {Y(f'{flesh}')}{Y('.')}")
            remaining_lives_block(
                black_knight_lives, player_shield_blocks, player, knight, Y, punc)

            # make a if statement to only write the battle ensues statement when limbs are 4 and blocks are 3, so it only goes once
            attack = player_attack(player_shield_blocks,
                                   black_knight_lives, player, Y)
            random_attack = cpu_random_attack(rock, paper, scissors)

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
                    tie(Y, knight)
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
