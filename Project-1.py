#!/usr/bin/env python3

"""This script will perform the game rock paper scissors"""

import random

import crayons


# this function will end the game when executed


def player_attack(player_shield_blocks, black_knight_lives, player, Y):
    input1 = input("    ").capitalize()

    if player_shield_blocks == 3 and black_knight_lives == 4 and (input1 == "Rock" or input1 == "Paper" or input1 == "Scissors" or input1 == "Flesh Wound"):
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


def black_knight_dismember_print(black_knight_lives, attack, random_attack, player, Y, punc, knight):

    if black_knight_lives == 3:
        black_knight_lives = print(f"\n\n\n{player}{Y(f' dodges the {knight}')}{Y(f'{punc}s ')}{random_attack}{Y(f' hand, steps aside, and cuts the {knight}{punc}')}{Y(f's left arm off with his ')}{crayons.blue(attack)}{Y(f' hand. Blood spurts from the knight{punc}')}{Y('s open shoulder.')}\n\n{player}{Y(': Now stand aside, worthy adversary.')}\n{knight}{Y(f': {punc}Tis but a scratch.')}\n{player}{Y(f': A SCRATCH? Your arm{punc}')}{Y('s off!')}\n{knight}{Y(f': No it isn{punc}')}{Y('t!')}\n{player}{Y(f': Well what{punc}')}{Y('s that then? (pointing to the arm lying on the ground)')}\n{knight}{Y(f': I{punc}')}{Y('ve had worse.')}\n{player}{Y(': You LIAR!')}\n{knight}{Y(': Come on, you pansy!')}\n")
        return black_knight_lives
    elif black_knight_lives == 2:
        black_knight_lives = print(f"\n\n\n{player}{Y(f' dodges the {knight}')}{Y(f'{punc}s swift')} {random_attack} {Y(f'kick!')} {player} {Y(f'easily cuts off the ')}{knight}{punc}{Y(f's right arm causing it to drop to the ground. Blood spatters freely from the stump.')}\n\n{knight}{Y(f': Come on then!')}\n{player}{Y(f': What?!?')}\n{knight}{Y(f': Have at you!')}\n{player}{Y(f': You are indeed brave, sir knight, but the fight is mine!.')}\n{knight}{Y(f': Ohhh, had enough, eh?')}\n{player}{Y(f': Look, you stupid bastard, you{punc}')}{Y(f've got no arms left!')}\n{knight}{Y(f': Yes I have!')}\n{player}{Y(f': LOOK!!!')}\n{knight}{Y(f': Just a flesh wound!')}")
        return black_knight_lives
    elif black_knight_lives == 1:
        black_knight_lives = print(f"\n\n\n{player}{Y(f' dodges the {knight}')}{Y(f'{punc}s single-legged')} {random_attack} {Y(f'kick!')} \n\n{player}{Y(f': I{punc}ll have your leg!')} \n\n\n{Y(f'({player}')} {Y(f'chops off the {knight}')}{Y(f'{punc}s leg with his')} {attack} {Y('hand)')}\n\n{knight}{Y(f': (hopping) Right!  I{punc}')}{Y(f'll do you for that!')}\n{player}{Y(f': You{punc}ll *WHAT*?')}\n{knight}{Y(f': Come {punc}ere!')}")
        return black_knight_lives
    elif black_knight_lives == 0:
        black_knight_lives = print(f"\n\n{player}{Y(f': (tiring of this)  What{punc}re you going to do, bleed on me?')}\n{knight}{Y(f': I{punc}m *INVINCIBLE*!!!')} \n{Y(f'{player}')} {Y(f': You{punc}re a looney....')}\n{knight}{Y(f': The {knight}')} {Y(f'ALWAYS TRIUMPHS! Have at you!!')} \n\n{Y(f'(hopping around, trying to kick {player}')} {Y(f'with his one remaining leg) {player}')}{Y(f' shrugs his shoulders and, with a mighty swing, removes the {knight}')}{Y(f'{punc}')}{Y(f's last appendage. The Knight falls to the ground. He looks about, realizing he can{punc}')}{Y(f't move.')}\n\n{player}{Y(f': Okay, we{punc}ll call it a draw. Come, Pasty! (they {punc}ride{punc} away)')}\n{knight}{Y(f': (calling after them) Oh! Had enough, eh? Come back and take what{punc}s coming to you, you yellow bastards!! Come back here and take what{punc}s coming to you! {punc}ll bite your legs off!')}")
        return black_knight_lives

# {Y(f': <tiring of this>  What{punc}re you going to do, bleed on me?')}\n{knight}{Y(f': I{punc}m *INVINCIBLE*!!!.')}\n{player}{Y(f'You{punc}re a looney....')}\n{knight}{Y(f': The Black Knight ALWAYS TRIUMPHS! Have at you!! <hopping around, trying to kick {player} with his one remaining leg>')


def player_blocks_print(blocks_left, random_attack, answer_king_queen, black_knight_lives, player_shield_blocks, player, Y, knight, punc):

    if player_shield_blocks == 2 and black_knight_lives > 2:
        blocks_left = print(
            f"\n{Y('The')} {knight} {Y(f'dodges {player}')}{Y(f'{punc}')}{Y(f's strike, and hurls his {random_attack}')} {Y(f'hand at {player}')}{Y('.')}\n\n{player} {Y(f'blocks the {knight}')}{Y(f'{punc}')}{Y(f's {random_attack} ')}{Y(f'but remains unscathed!')}\n\n{player}{Y(f': Aha! You are as weak as I thought!')}\n{knight}{Y(f': None before have passed! You')}{Y(f'{punc}ll see!')}\n")
        return blocks_left
    elif player_shield_blocks == 2 and black_knight_lives <= 2:
        blocks_left = print(
            f"\n{Y('S urpisingly fast for having no arms, the')} {knight} {Y(f'dodges {player}')}{Y(f'{punc}')}{Y(f's strike, and kicks his {random_attack}')} {Y(f'foot at {player}')}{Y('.')}\n\n{player} {Y(f'blocks the {knight}')}{Y(f'{punc}')}{Y(f's {random_attack} ')}{Y(f'but remains unscathed!')}\n\n{player}{Y(f': Aha! You are as weak as I thought!')}\n{knight}{Y(f': None before have passed! You')}{Y(f'{punc}ll see!')}\n")
        return blocks_left
    elif player_shield_blocks == 1 and black_knight_lives > 2:
        blocks_left = print(
            f"\n{Y('Once again the')} {knight} {Y(f'dodges {player}')}{Y(f'{punc}')}{Y(f's strike, and catapult{punc}')}{Y(f's his {random_attack}')} {Y(f'hand at {player}')}{Y('.')}\n\n{player} {Y(f'varely blocks the {knight}')}{Y(f'{punc}')}{Y(f's {random_attack} ')}{Y(f'and stumbles backwards from the blow!')}\n\n{player}{Y(f': That was a clsoe one sir knight! But I am a')}\n{answer_king_queen}{Y(f', do you think I would be so easily conquered?')}\n")
        return blocks_left
    elif player_shield_blocks == 1 and black_knight_lives > 2:
        blocks_left = print(
            f"\n{Y('Once again the')} {knight} {Y(f'dodges {player}')}{Y(f'{punc}')}{Y(f's strike, and super kicks his {random_attack}')} {Y(f'foot at {player}')}{Y('.')}\n\n{player} {Y(f'barely blocks the {knight}')}{Y(f'{punc}')}{Y(f's {random_attack} ')}{Y(f'and stumbles backwards from the blow!')}\n\n{player}{Y(f': That was a clsoe one sir knight! But I am a')}\n{answer_king_queen}{Y(f', do you think I would be so easily conquered?')}\n{knight}{Y(f': You will soon fall to the legless {knight}')}{Y('!')}\n")
        return blocks_left
    elif player_shield_blocks == 0 and black_knight_lives > 2:
        blocks_left = print(
            f"\n{Y('The')} {knight} {Y(f'dances around {player}')}{Y(f'{punc}')}{Y(f's strike, and strikes {player}')} {Y(f'with his {random_attack}')} {Y(f'hand.')}\n\n{player} {Y(f' blocks the {random_attack}')} {Y(f'and is knocked over onto the ground, destroying the {answer_king_queen}')}{Y(f'{punc}')}{Y('s shield in the process')}\n\n{player}{Y(f': (getting up) I suggest you enjoy this moment while it lasts, because this will be your last!')}\n{knight}{Y(f'What happened? Is {player}')}{Y(f', noble {answer_king_queen}')}{Y('of the Britons')} {Y(f'scared now?!')}{player}{Y(f': You{punc}')}{Y('ll pay for mocking the throne!')}\n")
        return blocks_left
    elif player_shield_blocks == 0 and black_knight_lives <= 2:
        blocks_left = print(
            f"\n{Y('The')} {knight} {Y(f'dances around {player}')}{Y(f'{punc}')}{Y(f's strike, and jump kicks {player}')} {Y(f'with his {random_attack}')} {Y(f'foot.')}\n\n{player} {Y(f' blocks the {random_attack}')} {Y(f', but is knocked over onto the ground, destroying the {answer_king_queen}')}{Y(f'{punc}')}{Y('s shield in the process')}\n\n{player}{Y(f': (getting up) I suggest you enjoy this moment while it lasts, because this will be your last!')}\n{knight}{Y(f'What happened? Is {player}')}{Y(f', noble {answer_king_queen}')}{Y('of the Britons')} {Y(f'scared now?!')}{player}{Y(f': You{punc}')}{Y('ll pay for mocking the throne!')}\n")
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
                    f"\n\n\n{Y('(clop clop clop)')}\n\n{Y('(clop clop clop)')}\n\n{Y('(clop clop clop)')}\n\n{Y('chhange this to the script of seeing black knight fight at bridge!')}\n\n\n\n{Y(f'{knight}')}{Y(': NONE SHALL PASS.')}\n\n{Y(f'{player}')}{Y(': (taken aback) What?')}\n\n{Y(f'{knight}')}{Y(': NONE SHALL PASS.')}\n\n{Y(f'{player}')}{Y(': I have no quarrel with you, good sir knight, but I must cross this bridge.')}\n\n{Y(f'{knight}')}{Y(': THEN YOU SHALL DIE.')}\n\n{Y(f'{player}')}{Y(f': I *command* you, as {answer_king_queen}')}{Y(' of the Britons, to stand aside.')}\n\n{Y(f'{knight}')}{Y(f': I MOVE FOR NO {answer_king_queen.upper()}')}{Y('.')}\n\n{Y(f'{player}')}{Y(': So be it!   (draws hand and shield)')}")
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

            if attack != "Rock" and attack != "Paper" and attack != "Scissors" and attack != "Flesh Wound":
                print(
                    f"rock boy")

            if attack == "Rock":
                print(
                    f"\n\n\n{answer_king_queen} {player} {Y(f'strikes the {knight}')}{Y(f' with a very hard {attack}')}{Y(f'... the the {knight}')} {Y(f'simultaneously strikes back with his {random_attack}')}")

                if random_attack == (f"{scissors}"):
                    # print black night saying oh no my arms! etc until dead
                    black_knight_lives -= 1
                    black_knight_dismember_print(
                        black_knight_lives, attack, random_attack, player, Y, punc, knight)
                    # remaining_lives_block(
                    #     black_knight_lives, player_shield_blocks, player)
                elif random_attack == (f"{paper}"):
                    player_shield_blocks -= 1
                    player_blocks_print(
                        player_shield_blocks, random_attack, answer_king_queen, black_knight_lives, player_shield_blocks, player, Y, knight, punc)
                    # remaining_lives_block(
                    #     black_knight_lives, player_shield_blocks, player)
                elif random_attack == (f"{rock}"):
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
