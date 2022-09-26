#!/usr/bin/env python3

"""This script will perform the game rock paper scissors"""
import random
import crayons
from time import sleep
import sys
# this function will end the game when executed


def player_attack():
    input1 = input("    ").strip().capitalize()
    return input1


def print_commence_battle(player_shield_blocks, black_knight_limbs, player, Y, random_attack, attack, knight):
    if player_shield_blocks == 3 and black_knight_limbs == 4 and (attack != random_attack) and (attack == "Rock" or attack == "Paper" or attack == "Scissors" or attack == "Flesh wound"):
        print(
            f"\n{Y(f'A battle ensues, where {player}')}{Y(f', realitvely unencumbered by armor, has an advantage at dodging the slow heavy strikes by the {knight}')}{Y(f'.')}")


def print_tie(Y, knight):
    print(f"\n{knight}{Y(': Ah foe, you think you can equal my strength?! Accept your luck. It will run out!')}")


def print_exit_game(Y, punc):
    print(f"\n\n\n{Y('Oh! Had enough, eh?')}\n{Y(f'Come back and take what{punc}s coming to you, you yellow bastard!')}\n{Y(f'Come back here and take what{punc}s coming to you!')}\n\n{Y(f'I{punc}ll bite your legs off!')}")


def print_remaining_lives_block(black_knight_limbs, player_shield_blocks, player, knight, Y, answer_king_queen):
    print(
        f"{knight} {Y(f'Limbs Remaining: {black_knight_limbs}')}\n{answer_king_queen} {player}{Y(' Shield Blocks Remaining: ')}{Y(f'{player_shield_blocks}')}")


def pick_name(Y, punc, C, R):
    name = ""
    while name != "Exit":
        print(f"{Y('Please enter your name: ')}")
        name = input("    ").strip().capitalize()

        if name == "Exit":
            print_exit_game(Y, punc)
            quit()
        elif len(name) > 2:
            break
        else:
            spacing()
            print(
                f"{R('Your name must be')} {C('3')} {R('characters at a minimum!')}")

    return crayons.cyan(name)


def pick_king_queen(Y, punc, R):
    # global king_queen
    king_queen = ""
    king = crayons.cyan("King")
    queen = crayons.cyan("Queen")

    while king_queen != "King" or king_queen != "Queen":
        print(f"{Y(f'Would you prefer to be a {king}')} {Y(f'or a {queen}')}{Y('? ')}")
        king_queen = input("    ").strip().capitalize()

        if king_queen == "King" or king_queen == "Queen":
            break
        elif king_queen == "Exit":
            print_exit_game(Y, punc)
            quit()
        else:
            spacing()
            print(
                f"{R(f'Please enter {punc}{king}')}{R(f'{punc} or {punc}')}{R(f'{queen}')}{R(f'{punc}.')}")
    return crayons.cyan(king_queen)


def cpu_random_attack(rock, paper, scissors):
    attack_choices = ((f"{rock}"), (f"{paper}"), (f"{scissors}"))
    random_attack = random.choice(attack_choices)
    return random_attack


def print_black_knight_dismember(black_knight_limbs, attack, random_attack, player, Y, punc, knight, answer_king_queen, C):

    if black_knight_limbs == 7:
        limbs_left = print(f"\n{answer_king_queen} {player}{Y(f' dodges the {knight}')}{Y(f'{punc}s ')}{random_attack}{Y(f' hand, steps aside, and cuts on of the {knight}{punc}')}{Y(f's additional appendages off with his {attack}')}\n\n{answer_king_queen} {player}{Y(f': You are no longer an 8 legged freak, soon to be no legged!')}\n{knight}{Y(f': A {answer_king_queen}')} {Y('can dream I suppose!')}")
    elif black_knight_limbs == 6:
        limbs_left = print(f"\n{answer_king_queen} {player}{Y(f' dodges the {knight}')}{Y(f'{punc}s ')}{random_attack}{Y(f' hand, steps aside, and cuts on of the {knight}{punc}')}{Y(f's additional appendages off with his {attack}')}\n\n{knight}{Y(f': Silly {answer_king_queen}')}{Y(f'... Trying to undo what you have done, eh?')}\n{answer_king_queen} {player}{Y(f': AND succeeding!')}")
    elif black_knight_limbs == 5:
        limbs_left = print(f"\n{answer_king_queen} {player}{Y(f' dodges the {knight}')}{Y(f'{punc}s ')}{random_attack}{Y(f' hand, steps aside, and cuts on of the {knight}{punc}')}{Y(f's additional appendages off with his {attack}')}\n\n{answer_king_queen} {player}{Y(': You are lucky I blessed you with greater strength, sir knight! I can take them away just as easily as I gave them!')}")
        return limbs_left
    elif black_knight_limbs == 4:
        limbs_left = print(f"\n{answer_king_queen} {player}{Y(f' dodges the {knight}')}{Y(f'{punc}s ')}{random_attack}{Y(f' hand, steps aside, and cuts the {knight}{punc}')}{Y(f's additional appendage off with his {attack}')}\n\n{answer_king_queen} {player}{Y(': Phew! It was about time I fixed that, prepare for your worst!.')}\n{knight}{Y(f': {punc}What are you going to do, {answer_king_queen}')}{Y(f'? Give me another arm again?!')}\n{answer_king_queen} {player}{Y(f': Never!')}")
        return limbs_left
    elif black_knight_limbs == 3:
        limbs_left = print(f"\n{answer_king_queen} {player}{Y(f' dodges the {knight}')}{Y(f'{punc}s ')}{random_attack}{Y(f' hand, steps aside, and cuts the {knight}{punc}')}{Y(f's left arm off with his {attack}')}{Y(f' hand. Blood spurts from the knight{punc}')}{Y('s open shoulder.')}\n\n{answer_king_queen} {player}{Y(': Now stand aside, worthy adversary.')}\n{knight}{Y(f': {punc}Tis but a scratch.')}\n{answer_king_queen} {player}{Y(f': A SCRATCH? Your arm{punc}')}{Y('s off!')}\n{knight}{Y(f': No it isn{punc}')}{Y('t!')}\n{answer_king_queen} {player}{Y(f': Well what{punc}')}{Y('s that then? (pointing to the arm lying on the ground)')}\n{knight}{Y(f': I{punc}')}{Y('ve had worse.')}\n{answer_king_queen} {player}{Y(': You LIAR!')}\n{knight}{Y(': Come on, you pansy!')}")
        return limbs_left
    elif black_knight_limbs == 2:
        limbs_left = print(f"\n{answer_king_queen} {player}{Y(f' dodges the {knight}')}{Y(f'{punc}s swift')} {random_attack} {Y(f'kick!')} {player} {Y(f'easily cuts off the ')}{knight}{Y(f'{punc}s right arm causing it to drop to the ground. Blood spatters freely from the stump.')}\n\n{knight}{Y(f': Come on then!')}\n{answer_king_queen} {player}{Y(f': What?!?')}\n{knight}{Y(f': Have at you!')}\n{answer_king_queen} {player}{Y(f': You are indeed brave, sir knight, but the fight is mine!.')}\n{knight}{Y(f': Ohhh, had enough, eh?')}\n{player}{Y(f': Look, you stupid bastard, you{punc}')}{Y(f've got no arms left!')}\n{knight}{Y(f': Yes I have!')}\n{answer_king_queen} {player}{Y(f': LOOK!!!')}\n{knight}{Y(f': Just a flesh wound!')}")
        return limbs_left
    elif black_knight_limbs == 1:
        limbs_left = print(f"\n{answer_king_queen} {player}{Y(f' dodges the {knight}')}{Y(f'{punc}s single-legged')} {random_attack} {Y(f'kick!')} \n\n{answer_king_queen} {player}{Y(f': I{punc}ll have your leg!')} \n\n\n{Y(f'(')}{answer_king_queen} {player} {Y(f'chops off the {knight}')}{Y(f'{punc}s leg with his')} {attack} {Y('hand)')}\n\n{knight}{Y(f': (hopping) Right!  I{punc}')}{Y(f'll do you for that!')}\n{answer_king_queen} {player}{Y(f': You{punc}ll *WHAT*?')}\n{knight}{Y(f': Come {punc}ere!')}")
        return limbs_left
    elif black_knight_limbs == 0:
        limbs_left = print(f"\n{answer_king_queen} {player}{Y(f': (tiring of this)  What{punc}re you going to do, bleed on me?')}\n{knight}{Y(f': I{punc}m *INVINCIBLE*!!!')} \n{Y(f'{answer_king_queen} {player}')} {Y(f': You{punc}re a looney....')}\n{knight}{Y(f': The {knight}')} {Y(f'ALWAYS TRIUMPHS! Have at you!!')} {Y(f'(hopping around, trying to kick {answer_king_queen} {player}')} {Y(f'with his one remaining leg)')} \n\n{answer_king_queen} {player} {Y(f'shrugs his shoulders and, with a mighty swing, removes the {knight}')}{Y(f'{punc}')}{Y(f's last appendage. The Knight falls to the ground. He looks about, realizing he can{punc}')}{Y(f't move.')}\n\n{answer_king_queen} {player}{Y(f': Okay, we{punc}ll call it a draw. Come, Pasty! (')}{answer_king_queen} {player} {Y(f'{punc}rides{punc} away)')}\n{knight}{Y(f': (calling after them) Oh! Had enough, eh? Come back and take what{punc}s coming to you, you yellow bastards!! Come back here and take what{punc}s coming to you! I{punc}ll bite your legs off!')}\n\n\n{C('Congratulations')} {answer_king_queen} {player}{C('!')} {Y(f'You have conquered the')} {knight} {Y('and can continue on your journey to finding the')} {C('Holy Grail')}{Y('!')}")
        return limbs_left


def print_player_blocks(player_shield_blocks, random_attack, answer_king_queen, black_knight_limbs, player, Y, knight, punc, attack, C, R):

    if player_shield_blocks == 2 and black_knight_limbs >= 5:
        blocks_left = print(
            f"\n{Y('The')} {knight} {Y(f'begins spinning all of his')} {random_attack} {Y(f'arms at')} {answer_king_queen} {player} {Y(f'while dodging the')} {answer_king_queen}{Y(f'{punc}s {attack}')}\n\n{answer_king_queen} {player} {Y(f'blocks the {knight}')}{Y(f'{punc}')}{Y(f's whirlwind {random_attack}')} {Y(f'hands but remains unscathed!')}\n\n{answer_king_queen} {player}{Y(f': Aha! You are as weak as I thought!')}\n{knight}{Y(f': None before have passed! You')}{Y(f'{punc}ll see!')}\n")
        return blocks_left
    elif player_shield_blocks == 2 and (black_knight_limbs > 2 and black_knight_limbs <= 4):
        blocks_left = print(
            f"\n{Y('The')} {knight} {Y(f'dodges {answer_king_queen} {player}')}{Y(f'{punc}')}{Y(f's strike, and hurls his {random_attack}')} {Y(f'hand at {answer_king_queen} {player}')}{Y('.')}\n\n{answer_king_queen} {player} {Y(f'blocks the {knight}')}{Y(f'{punc}')}{Y(f's {random_attack} ')}{Y(f'but remains unscathed!')}\n\n{answer_king_queen} {player}{Y(f': Aha! You are as weak as I thought!')}\n{knight}{Y(f': None before have passed! You')}{Y(f'{punc}ll see!')}\n")
        return blocks_left
    elif player_shield_blocks == 2 and black_knight_limbs <= 2:
        blocks_left = print(
            f"\n{Y('Surpisingly fast for having no arms, the')} {knight} {Y(f'dodges {answer_king_queen} {player}')}{Y(f'{punc}')}{Y(f's strike, and kicks his {random_attack}')} {Y(f'foot at {answer_king_queen} {player}')}{Y('.')}\n\n{answer_king_queen} {player} {Y(f'blocks the {knight}')}{Y(f'{punc}')}{Y(f's {random_attack} ')}{Y(f'but remains unscathed!')}\n\n{answer_king_queen} {player}{Y(f': Aha! You are as weak as I thought!')}\n{knight}{Y(f': None before have passed! You')}{Y(f'{punc}ll see!')}\n")
        return blocks_left

    elif player_shield_blocks == 2 and black_knight_limbs >= 5:
        blocks_left = print(
            f"\n{Y('The')} {knight} {Y(f'begins spinning all of his')} {random_attack} {Y(f'arms at')} {answer_king_queen} {player} {Y(f'while dodging the')} {answer_king_queen}{Y(f'{punc}s {attack}')}\n\n{answer_king_queen} {player} {Y(f'barely blocks the {knight}')}{Y(f'{punc}')}{Y(f's whirlwind {random_attack}')} {Y(f'hands and stumbles backwards from the blow!')}\n\n{answer_king_queen} {player}{Y(f': That was a close one sir knight! But I am a')} {answer_king_queen}{Y(f', do you think I would be so easily conquered?')}\n{knight}{Y(f': You will soon fall to the fearless {knight}')}{Y('!')}\n")
        return blocks_left
    elif player_shield_blocks == 1 and (black_knight_limbs > 2 and black_knight_limbs <= 4):
        blocks_left = print(
            f"\n{Y('Once again the')} {knight} {Y(f'dodges {answer_king_queen} {player}')}{Y(f'{punc}')}{Y(f's strike, and catapult{punc}')}{Y(f's his {random_attack}')} {Y(f'hand at {player}')}{Y('.')}\n\n{answer_king_queen} {player} {Y(f'barely blocks the {knight}')}{Y(f'{punc}')}{Y(f's {random_attack} ')}{Y(f'and stumbles backwards from the blow!')}\n\n{answer_king_queen} {player}{Y(f': That was a close one sir knight! But I am a')} {answer_king_queen}{Y(f', do you think I would be so easily conquered?')}\n{knight}{Y(f': You will soon fall to the fearless {knight}')}{Y('!')}\n")
        return blocks_left
    elif player_shield_blocks == 1 and black_knight_limbs < 2:
        blocks_left = print(
            f"\n{Y('Once again the')} {knight} {Y(f'dodges {answer_king_queen} {player}')}{Y(f'{punc}')}{Y(f's strike, and super kicks his {random_attack}')} {Y(f'foot at {answer_king_queen} {player}')}{Y('.')}\n\n{answer_king_queen} {player} {Y(f'barely blocks the {knight}')}{Y(f'{punc}')}{Y(f's {random_attack} ')}{Y(f'and stumbles backwards from the blow!')}\n\n{answer_king_queen} {player}{Y(f': That was a close one sir knight! But I am a')} {answer_king_queen}{Y(f', do you think I would be so easily conquered?')}\n{knight}{Y(f': You will soon fall to the legless {knight}')}{Y('!')}\n")
        return blocks_left

    elif player_shield_blocks == 2 and black_knight_limbs >= 5:
        blocks_left = print(
            f"\n{Y('The')} {knight} {Y(f'begins spinning all of his')} {random_attack} {Y(f'arms at')} {answer_king_queen} {player} {Y(f'while dodging the')} {answer_king_queen}{Y(f'{punc}s {attack}')}\n\n{answer_king_queen} {player} {Y(f'blocks the {knight}')}{Y(f'{punc}')}{Y(f's whirlwind {random_attack}')} {Y(f'and is knocked over onto the ground, destroying the {answer_king_queen}')}{Y(f'{punc}')}{Y('s shield in the process.')}\n\n{answer_king_queen} {player}{Y(f': (getting up) I suggest you enjoy this moment while it lasts, because this will be your last!')}\n{knight}{Y(f': What happened? Is {player}')}{Y(f', noble {answer_king_queen}')} {Y('of the Britons')} {Y(f'scared now?!')}\n{answer_king_queen} {player}{Y(f': You{punc}')}{Y('ll pay for mocking the throne!')}\n")
    elif player_shield_blocks == 0 and (black_knight_limbs > 2 and black_knight_limbs <= 4):
        blocks_left = print(
            f"\n{Y('The')} {knight} {Y(f'dances around {answer_king_queen} {player}')}{Y(f'{punc}')}{Y(f's strike, and strikes {answer_king_queen} {player}')} {Y(f'with his {random_attack}')} {Y(f'hand.')} {answer_king_queen} {player} {Y(f'blocks the {random_attack}')} {Y(f'and is knocked over onto the ground, destroying the {answer_king_queen}')}{Y(f'{punc}')}{Y('s shield in the process.')}\n\n{answer_king_queen} {player}{Y(f': (getting up) I suggest you enjoy this moment while it lasts, because this will be your last!')}\n{knight}{Y(f': What happened? Is {player}')}{Y(f', noble {answer_king_queen}')} {Y('of the Britons')} {Y(f'scared now?!')}\n{answer_king_queen} {player}{Y(f': You{punc}')}{Y('ll pay for mocking the throne!')}\n")
        return blocks_left
    elif player_shield_blocks == 0 and black_knight_limbs <= 2:
        blocks_left = print(
            f"\n{Y('The')} {knight} {Y(f'dances around {answer_king_queen} {player}')}{Y(f'{punc}')}{Y(f's strike, and jump kicks {answer_king_queen} {player}')} {Y(f'with his {random_attack}')} {Y(f'foot.')}\n\n{answer_king_queen} {player} {Y(f' blocks the {random_attack}')} {Y(f', but is knocked over onto the ground, destroying the {answer_king_queen}')}{Y(f'{punc}')}{Y('s shield in the process')}\n\n{answer_king_queen} {player}{Y(f': (getting up) I suggest you enjoy this moment while it lasts, because this will be your last!')}\n{knight}{Y(f': What happened? Is {player}')}{Y(f', noble {answer_king_queen}')} {Y('of the Britons')} {Y(f'scared now?!')}\n{answer_king_queen} {player}{Y(f': You{punc}')}{Y('ll pay for mocking the throne! Just you wait!')}\n")
        return blocks_left

    elif player_shield_blocks == -1 and black_knight_limbs >= 5:
        blocks_left = print(
            f"\n{Y('The')} {knight} {Y(f'begins spinning all of his')} {random_attack} {Y(f'arms at')} {answer_king_queen} {player} {Y(f'while dodging the')} {answer_king_queen}{Y(f'{punc}s')} {attack} {Y('hand.')}\n{Y('The')} {knight} {Y(f'in a fury of')} {random_attack} {Y(f'slashes, proceeds to puncture {answer_king_queen} {player}')} {Y(f'a multitude of times, knocking the {answer_king_queen} on both knees.')}\n\n{knight}{Y(f': Well,')} {answer_king_queen} {player}{Y(f', it seems you shall not pass afterall.')}\n{answer_king_queen} {player}{Y(f': (coughing and unable to speak well) It seems so... fair knight... I have... underestima... ({answer_king_queen} {player}')} {Y('dies)')}\n{knight}{Y(f': RIP lol')}\n\n\n{R('GAME OVER')} {answer_king_queen} {player}{C('!')} {Y(f'You have fallen to the')} {knight} {Y('and will never continue on to find the')} {C('Holy Grail')}{Y('!')}")
    elif player_shield_blocks == -1 and (black_knight_limbs > 2 and black_knight_limbs <= 4):
        blocks_left = print(
            f"\n{Y('The')} {knight} {Y(f'easily predicts {answer_king_queen} {player}')}{Y(f'{punc}s strike and counters the {answer_king_queen}')}{Y(f'{punc}s')} {attack} {Y(f'hand with a blazingly fast {random_attack}')}{Y('hand, puncturing the')} {answer_king_queen} {Y(f'a multitude of times. {answer_king_queen} {player} falls on both knees.')}\n\n{knight}{Y(f': Well,')} {answer_king_queen} {player}{Y(f', it seems you shall not pass afterall.')}\n{answer_king_queen} {player}{Y(f': (coughing and unable to speak well) It seems so... fair knight... I have... underestima... ({answer_king_queen} {player}')} {Y('dies)')}\n{knight}{Y(f': RIP lol')}\n\n\n{C('GAME OVER')} {answer_king_queen} {player}{C('!')} {Y(f'You have fallen to the')} {knight} {Y('and will never continue on to find the')} {C('Holy Grail')}{Y('!')}")
        return blocks_left
    elif player_shield_blocks == -1 and black_knight_limbs <= 2:
        blocks_left = print(
            f"\n{Y('The')} {knight} {Y(f'easily predicts {answer_king_queen} {player}')} {Y(f'strike and counters the {answer_king_queen}')}{Y(f'{punc}s')} {attack} {Y(f'hand with a blazingly fast, single-legged, jumping {random_attack}')} {Y('kick.')} \n{Y('The')} {answer_king_queen}{Y(f', hit with such force, falls on both knees.')}\n\n{knight}{Y(f': Well,')} {answer_king_queen} {player}{Y(f', it seems you shall not pass afterall.')}\n{answer_king_queen} {player}{Y(f': (coughing and unable to speak well) It seems so... fair knight... I have... underestima... ({answer_king_queen} {player}')} {Y('dies)')}\n{knight}{Y(f': RIP lol')}\n\n\n{C('GAME OVER')} {answer_king_queen} {player}{C('!')} {Y(f'You have fallen to the')} {knight} {Y('and will never continue on to find the')} {C('Holy Grail')}{Y('!')}")
        return blocks_left


def print_game_instructions(rock, paper, scissors, flesh, C, knight, Y, punc, R):
    print(f"\n\n{Y('Welcome to')} {rock}{Y(',')} {paper}{Y(',')} {scissors}{Y(',')} {flesh}{Y('.')}\n\n      {Y(f'In this game')} {C('you')} {Y(f'will be playing against the {knight}')} {Y('from Monty Python and the Holy Grail.')}\n      {Y(f'The goal is to to beat the {knight}')} {Y('and cross the bridge by choosing 1 of the 4 options available:')}\n\n{rock}{Y(':')}\n   {Y('Wins against')} {scissors}\n   {Y('Loses against')} {paper}\n\n{paper}{Y(':')}\n   {Y('Wins against')} {rock}\n   {Y('Loses against')} {scissors}\n\n{scissors}{Y(':')}\n   {Y('Wins against')} {paper}\n   {Y('Loses against')} {rock}\n\n{flesh}{Y(':')}\n   {Y('You will see...')}\n\n\n")
    print(
        f"{Y('Please enter:')}\n   {Y(f'{punc}')}{C('1')}{Y(f'{punc} to continue!')}\n   {Y(f'{punc}')}{C('Exit')}{Y(f'{punc} to end your journey.')}")
    continue_exit = ""

    while (continue_exit != 1 or continue_exit != "Exit"):
        continue_exit = input("    ").strip()
        input2 = ""
        if continue_exit.isdigit():
            input2 = int(continue_exit)
        elif continue_exit.capitalize() == "Exit":
            print_exit_game(Y, punc)
            quit()
        if input2 == 1:
            break
        else:
            print_game_start_repeat(punc, C, R)


def print_game_start(answer_king_queen, player, punc, C, Y):
    print(f"\n{Y('Okay')} {answer_king_queen} {player}{Y(f', Let{punc}s go ahead and start the adventure!')}\n\n{Y('Please enter:')}\n   {Y(f'{punc}')}{C('1')}{Y(f'{punc} to grab your coconuts and gallop away!')}\n   {C(f'(You can enter {punc}Exit{punc} at any time during the game to leave)')}")


def print_game_start_repeat(punc, C, R):
    print(
        f"\n{R(f'Please enter: {punc}')}{C('1')}{R(f'{punc} or {punc}')}{C('Exit')}{R(f'{punc}.')}")


def print_choose_attack(rock, paper, scissors, flesh, Y):
    print(
        f"\n{Y('Choose your attack: ')}{Y(f'{rock}')}{Y(',')} {Y(f'{paper}')}{Y(',')} {Y(f'{scissors}')}{Y(',')} {Y(f'{flesh}')}{Y('.')}")


def print_choose_attack_repeat(rock, paper, scissors, flesh, R, punc):
    print(f"\n{R('Please enter:')} {R(f'{punc}{rock}')}{R(f'{punc}')}{R(',')} {R(f'{punc}{paper}')}{R(f'{punc}')}{R(',')} {R(f'{punc}{scissors}')}{R(f'{punc}')}{R(', or')} {R(f'{punc}{flesh}')}{R(f'{punc}')}{R('.')}")


def print_clop_journey_starts(knight, player, answer_king_queen, Y, punc, paper, scissors):
    print(
        f"\n\n\n{Y('(clop clop clop)')}\n\n{Y('(clop clop clop)')}\n\n{Y('(clop clop clop)')}\n\n{answer_king_queen} {player} {Y(f'and his trusty servant Patsy {punc}ride{punc} along through the woods.')} {Y('Suddenly they come apon a stream crossing where two knights are battling in a heated duel with giant hands. One is dressed in green and one in black.')} {answer_king_queen} {player} {Y('stops and watches the fight.')} {Y(f'The two knights attempt to maul each other in many various ways and with many different tools of medieval weaponry.')} {Y(f'Finally, when the green knight is charging the black with a giant')} {paper} {Y('hand, the')} {knight} {Y(f'throws his')} {scissors} {Y(f'hand straight through the slit in the green knight{punc}s helmet.')} {Y('The green knight falls to the ground, bleeding profusely.')} {Y('The')} {knight} {Y('steps forward and pulls his')} {scissors} {Y('hand out of the helmet.')} {answer_king_queen} {player}{Y(f', impressed with the')} {knight}{Y(f'{punc}s fighting, motions to Patsy and they {punc}ride{punc} forward.')}\n\n{Y(f'{knight}')}{Y(': NONE SHALL PASS.')}\n{answer_king_queen} {player}{Y(': (taken aback) What?')}\n{Y(f'{knight}')}{Y(': NONE SHALL PASS.')}\n{answer_king_queen} {player}{Y(': I have no quarrel with you, good sir knight, but I must cross this bridge.')}\n{Y(f'{knight}')}{Y(': THEN YOU SHALL DIE.')}\n{answer_king_queen} {player}{Y(f': I *command* you, as {answer_king_queen}')}{Y(' of the Britons, to stand aside.')}\n{Y(f'{knight}')}{Y(f': I MOVE FOR NO {answer_king_queen.upper()}')}{Y('.')}\n{answer_king_queen} {player}{Y(': So be it!   (draws hand and shield)')}")


def player_attack_input(attack, answer_king_queen, player, knight, random_attack, rock, paper, scissors, Y, flesh, punc, R, percent, C):
    if attack == "Rock":
        attack = rock
        print(f"\n{answer_king_queen} {player} {Y(f'strikes the {knight}')}{Y(' with a very hard')} {attack}{Y(f'... the {knight}')} {Y(f'simultaneously strikes back with his {random_attack}')}")
        return attack
    elif attack == "Paper":
        attack = paper
        print(f"\n{answer_king_queen} {player} {Y(f'strikes the {knight}')}{Y(' with a very smooth')} {attack}{Y(f'... the {knight}')} {Y(f'simultaneously strikes back with his {random_attack}')}")
        return attack
    elif attack == "Scissors":
        attack = scissors
        print(f"\n{answer_king_queen} {player} {Y(f'strikes the {knight}')}{Y(' with a very sharp')} {attack}{Y(f'... the {knight}')} {Y(f'simultaneously strikes back with his {random_attack}')}")
        return attack
    elif attack == "Flesh wound":
        print(f"\n{Y('You have chosen')} {flesh}{Y(f'. This is a special attack that has it{punc}s consequences if used incorrectly.')}\n\n{Y('When using')} {flesh}{Y(', you have the option of choosing')} {C('2')} {Y('different attacks to use against the')} {knight}{Y('.')}\n{Y(f'You{punc}ll have a')} {C(f'66{percent}')} {Y('chance to win.')}\n{Y('Although... if one of your attacks is the same as the')} {knight}{Y(f'{punc}s attack,')} {C('AND')} {Y('your other attack loses to the')} {knight}{Y(f'{punc}s attack.')}\n{Y('You,')} {answer_king_queen} {player}{Y(', will lose')} {C('1')} {Y('block')} {C('AND')} {Y('the')} {knight} {Y(f'will gain')} {C('1')} {Y('extra limb!')}\n")

        while (attack != "Exit"):
            print(
                f"{Y(f'    Choose the')} {C('first')} {Y('attack you would like to perform:')}")
            flesh_1 = input("    ").strip().capitalize()
            if flesh_1 != "Rock" and flesh_1 != "Paper" and flesh_1 != "Scissors" and flesh_1 != "Exit":
                print(f"\n{R('Please enter:')} {R(f'{punc}{rock}')}{R(f'{punc}')}{R(',')} {R(f'{punc}{paper}')}{R(f'{punc}')}{R(',')} {R(f'{punc}{scissors}')}{R(f'{punc}')}{R(', or')} {R(f'{punc}')}{C('Exit')}{R(f'{punc}')}")
            elif flesh_1 == "Rock":
                pick_one = rock
                break
            elif flesh_1 == "Paper":
                pick_one = paper
                break
            elif flesh_1 == "Scissors":
                pick_one = scissors
                break
            elif flesh_1 == "Exit":
                print_exit_game(Y, punc)
                quit()

        while (attack != "Exit"):
            print(
                f"\n{Y(f'    Choose the')} {C('second')} {Y('attack you would like to perform:')}")
            flesh_2 = input("    ").strip().capitalize()

            if flesh_2 != "Rock" and flesh_2 != "Paper" and flesh_2 != "Scissors" and flesh_2 != "Exit" or flesh_1 == flesh_2:
                print(f"\n{R('Please enter:')} {R(f'{punc}{rock}')}{R(f'{punc}')}{R(',')} {R(f'{punc}{paper}')}{R(f'{punc}')}{R(',')} {R(f'{punc}{scissors}')}{R(f'{punc}')}{R(', or')} {R(f'{punc}')}{C('Exit')}{R(f'{punc}')}\n         {C('<')}{R(f'Both choices can{punc}t be the same')}{C('>')}")
            elif flesh_2 == "Rock":
                pick_two = rock
                break
            elif flesh_2 == "Paper":
                pick_two = paper
                break
            elif flesh_2 == "Scissors":
                pick_two = scissors
                break
            elif flesh_2 == "Exit":
                print_exit_game(Y, punc)
                quit()

        flesh_attack = (f"{flesh_1}/{flesh_2}")
        spacing()
        print(f"\n{answer_king_queen} {player} {Y(f'strikes the {knight}')}{Y(' with a')} {flesh}{Y(f'({pick_one}')}{Y(f'/')}{Y(f'{pick_two}')}{Y(f')... the {knight}')} {Y(f'simultaneously strikes back with his {random_attack}')}")
        return flesh_attack


def initial_attack_input(Y, punc):
    attack = input("    ").strip().capitalize()
    if attack == "Exit":
        print_exit_game(Y, punc)
        quit()
    return attack


def flesh_wound_win_lose(random_attack, rock, paper, scissors, answer_king_queen, player, flesh, punc, Y, knight, attack, black_knight_limbs, player_shield_blocks, C, R):
    if (random_attack == (f"{paper}") and (attack == "Rock/Paper" or attack == "Paper/Rock")) or (random_attack == (f"{rock}") and (attack == "Rock/Scissors" or attack == "Scissors/Rock")) or (random_attack == (f"{scissors}") and (attack == "Scissors/Paper" or attack == "Paper/Scissors")):
        black_knight_limbs += 1
        player_shield_blocks -= 1
        attack = flesh
        print_player_blocks(
            player_shield_blocks, random_attack, answer_king_queen, black_knight_limbs, player, Y, knight, punc, attack, C, R)
        print(
            f"\n{Y(f'Wow! {answer_king_queen} {player}')} {Y(f'... Even with a {flesh}')}{Y(f' you managed to lose a round to the {knight}')}")
        print(
            f"{knight}{Y(': gains 1 limb back')}\n{answer_king_queen} {player}{Y(f': loses one block')}")
    elif (random_attack == (f"{paper}") and (attack == "Scissors/Paper" or attack == "Scissors/Rock" or attack == "Rock/Scissors" or attack == "Paper/Scissors")) or (random_attack == (f"{rock}") and (attack == "Paper/Scissors" or attack == "Paper/Rock" or attack == "Scissors/Paper" or attack == "Rock/Paper")) or (random_attack == (f"{scissors}") and (attack == "Rock/Paper" or attack == "Rock/Scissors" or attack == "Paper/Rock" or attack == "Scissors/Rock")):

        black_knight_limbs -= 1
        attack = flesh
        print_black_knight_dismember(
            black_knight_limbs, attack, random_attack, player, Y, punc, knight, answer_king_queen, C)
        print(
            f"\n\n{Y(f'Don{punc}t feel too proud of yourself, {answer_king_queen} {player}')}{Y(f'... You had to use a {flesh}')}{Y(f' to get the job done.')}")
    return black_knight_limbs, player_shield_blocks


def normal_attack_win_lose(random_attack, scissors, attack, answer_king_queen, knight, punc, player, black_knight_limbs, player_shield_blocks, rock, paper, Y, C, R):
    if (random_attack == (f"{scissors}") and attack == rock) or (random_attack == (f"{rock}") and attack == paper) or (random_attack == (f"{paper}") and attack == scissors):
        black_knight_limbs -= 1
        print_black_knight_dismember(
            black_knight_limbs, attack, random_attack, player, Y, punc, knight, answer_king_queen, C)
    elif (random_attack == (f"{paper}") and attack == rock) or (random_attack == (f"{scissors}") and attack == paper) or (random_attack == (f"{rock}") and attack == scissors):
        player_shield_blocks -= 1
        print_player_blocks(
            player_shield_blocks, random_attack, answer_king_queen, black_knight_limbs, player, Y, knight, punc, attack, C, R)
    elif (random_attack == (f"{rock}") and attack == rock) or (random_attack == (f"{paper}") and attack == paper) or (random_attack == (f"{scissors}") and attack == scissors):
        print_tie(Y, knight)
    return black_knight_limbs, player_shield_blocks


def spacing():
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")


def game_loop_replay(punc, Y, C, R):
    answer = ""
    while answer != "Exit":
        print(f"\n{Y('Play again?')}")
        print(
            f"{Y('Please enter:')}\n   {Y(f'{punc}')}{C('1')}{Y(f'{punc} to play again!')}\n   {Y(f'{punc}')}{C('Exit')}{Y(f'{punc} to end your journy here.')}")
        answer = input("    ").strip()
        answer2 = ""
        if answer.isdigit():
            answer2 = int(answer)
        elif answer.capitalize() == "Exit":
            print_exit_game(Y, punc)
            quit()
        if answer2 == 1:
            main()
            break
        else:
            print_game_start_repeat(punc, C, R)


def main():
    input1 = ""
    punc = "'"
    percent = "%"
    Y = crayons.yellow
    R = crayons.red
    C = crayons.cyan
    rock = crayons.white('Rock')
    paper = crayons.green('Paper')
    scissors = crayons.blue('Scissors')
    flesh = crayons.red('Flesh Wound')
    knight = crayons.magenta('Black Knight')
    black_knight_limbs = 4
    player_shield_blocks = 3

    while input1 != "Exit":

        print_game_instructions(rock, paper, scissors,
                                flesh, C, knight, Y, punc, R)
        spacing()
        player = pick_name(Y, punc, C, R)
        spacing()
        answer_king_queen = pick_king_queen(Y, punc, R)
        spacing()
        print_game_start(answer_king_queen, player, punc, C, Y)

        while (input1 != 1 or input1 != "Exit"):
            input1 = input("    ").strip()
            input2 = ""
            if input1.isdigit():
                input2 = int(input1)
            elif input1.capitalize() == "Exit":
                print_exit_game(Y, punc)
                quit()
            if input2 == 1:
                print_clop_journey_starts(
                    knight, player, answer_king_queen, Y, punc, paper, scissors)
                break
            else:
                print_game_start_repeat(punc, C, R)

        while (input1 != "Exit"):
            if player_shield_blocks < 0 or black_knight_limbs == 0:
                break
            print_choose_attack(rock, paper, scissors, flesh, Y)
            print_remaining_lives_block(
                black_knight_limbs, player_shield_blocks, player, knight, Y, answer_king_queen)
            attack = initial_attack_input(Y, punc)
            spacing()
            random_attack = cpu_random_attack(rock, paper, scissors)
            print_commence_battle(
                player_shield_blocks, black_knight_limbs, player, Y, random_attack, attack, knight)

            if attack != "Rock" and attack != "Paper" and attack != "Scissors" and attack != "Flesh wound":
                print_choose_attack_repeat(
                    rock, paper, scissors, flesh, R, punc)

            attack = player_attack_input(
                attack, answer_king_queen, player, knight, random_attack, rock, paper, scissors, Y, flesh, punc, R, percent, C)

            normal_new_limb_block = normal_attack_win_lose(
                random_attack, scissors, attack, answer_king_queen, knight, punc, player, black_knight_limbs, player_shield_blocks, rock, paper, Y, C, R)

            black_knight_limbs = normal_new_limb_block[0]
            player_shield_blocks = normal_new_limb_block[1]

            flesh_wound_new_limb_block = flesh_wound_win_lose(
                random_attack, rock, paper, scissors, answer_king_queen, player, flesh, punc, Y, knight, attack, black_knight_limbs, player_shield_blocks, C, R)

            black_knight_limbs = flesh_wound_new_limb_block[0]
            player_shield_blocks = flesh_wound_new_limb_block[1]
        break

    game_loop_replay(punc, Y, C, R)


if __name__ == "__main__":
    main()

# TODO add new message when knight gains lives and loses them as well
