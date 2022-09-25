#!/usr/bin/env python3

"""This script will perform the game rock paper scissors"""
import random
import crayons
# this function will end the game when executed


def player_attack():
    input1 = input("    ").capitalize()
    return input1


def print_commence_battle(player_shield_blocks, black_knight_limbs, player, Y, random_attack, attack, knight):
    if player_shield_blocks == 3 and black_knight_limbs == 4 and (attack != random_attack):
        print(
            f"\n{Y(f'A battle ensues, where {player}')}{Y(f', realitvely unencumbered by armor, has an advantage at dodging the slow heavy strikes by the {knight}')}{Y(f'.')}")


def print_tie(Y, knight):
    print(f"\n{knight}{Y(': Ah foe, you think you can equal my strength?! Accept your luck. It will run out!')}")


def print_exit_game(Y, punc):
    print(f"\n\n\n{Y('Oh! Had enough, eh?')}\n{Y(f'Come back and take what{punc}s coming to you, you yellow bastard!')}\n{Y(f'Come back here and take what{punc}s coming to you!')}\n\n{Y(f'I{punc}ll bite your legs off!')}")


def print_remaining_lives_block(black_knight_limbs, player_shield_blocks, player, knight, Y, answer_king_queen):
    print(
        f"{knight} {Y(f'Limbs Remaining: {black_knight_limbs}')}\n{answer_king_queen} {player}{Y(' Shield Blocks Remaining: ')}{Y(f'{player_shield_blocks}')}")


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


def print_black_knight_dismember(black_knight_limbs, attack, random_attack, player, Y, punc, knight, answer_king_queen):

    if black_knight_limbs == 3:
        limbs_left = print(f"\n{answer_king_queen} {player}{Y(f' dodges the {knight}')}{Y(f'{punc}s ')}{random_attack}{Y(f' hand, steps aside, and cuts the {knight}{punc}')}{Y(f's left arm off with his {attack}')}{Y(f' hand. Blood spurts from the knight{punc}')}{Y('s open shoulder.')}\n\n{answer_king_queen} {player}{Y(': Now stand aside, worthy adversary.')}\n{knight}{Y(f': {punc}Tis but a scratch.')}\n{answer_king_queen} {player}{Y(f': A SCRATCH? Your arm{punc}')}{Y('s off!')}\n{knight}{Y(f': No it isn{punc}')}{Y('t!')}\n{answer_king_queen} {player}{Y(f': Well what{punc}')}{Y('s that then? (pointing to the arm lying on the ground)')}\n{knight}{Y(f': I{punc}')}{Y('ve had worse.')}\n{answer_king_queen} {player}{Y(': You LIAR!')}\n{knight}{Y(': Come on, you pansy!')}")
        return limbs_left
    elif black_knight_limbs == 2:
        limbs_left = print(f"\n{answer_king_queen} {player}{Y(f' dodges the {knight}')}{Y(f'{punc}s swift')} {random_attack} {Y(f'kick!')} {player} {Y(f'easily cuts off the ')}{knight}{Y(f'{punc}s right arm causing it to drop to the ground. Blood spatters freely from the stump.')}\n\n{knight}{Y(f': Come on then!')}\n{answer_king_queen} {player}{Y(f': What?!?')}\n{knight}{Y(f': Have at you!')}\n{answer_king_queen} {player}{Y(f': You are indeed brave, sir knight, but the fight is mine!.')}\n{knight}{Y(f': Ohhh, had enough, eh?')}\n{player}{Y(f': Look, you stupid bastard, you{punc}')}{Y(f've got no arms left!')}\n{knight}{Y(f': Yes I have!')}\n{answer_king_queen} {player}{Y(f': LOOK!!!')}\n{knight}{Y(f': Just a flesh wound!')}")
        return limbs_left
    elif black_knight_limbs == 1:
        limbs_left = print(f"\n{answer_king_queen} {player}{Y(f' dodges the {knight}')}{Y(f'{punc}s single-legged')} {random_attack} {Y(f'kick!')} \n\n{answer_king_queen} {player}{Y(f': I{punc}ll have your leg!')} \n\n\n{Y(f'(')}{answer_king_queen} {player} {Y(f'chops off the {knight}')}{Y(f'{punc}s leg with his')} {attack} {Y('hand)')}\n\n{knight}{Y(f': (hopping) Right!  I{punc}')}{Y(f'll do you for that!')}\n{answer_king_queen} {player}{Y(f': You{punc}ll *WHAT*?')}\n{knight}{Y(f': Come {punc}ere!')}")
        return limbs_left
    elif black_knight_limbs == 0:
        limbs_left = print(f"\n{answer_king_queen} {player}{Y(f': (tiring of this)  What{punc}re you going to do, bleed on me?')}\n{knight}{Y(f': I{punc}m *INVINCIBLE*!!!')} \n{Y(f'{answer_king_queen} {player}')} {Y(f': You{punc}re a looney....')}\n{knight}{Y(f': The {knight}')} {Y(f'ALWAYS TRIUMPHS! Have at you!!')} {Y(f'(hopping around, trying to kick {answer_king_queen} {player}')} {Y(f'with his one remaining leg)')} \n\n{answer_king_queen} {player} {Y(f'shrugs his shoulders and, with a mighty swing, removes the {knight}')}{Y(f'{punc}')}{Y(f's last appendage. The Knight falls to the ground. He looks about, realizing he can{punc}')}{Y(f't move.')}\n\n{answer_king_queen} {player}{Y(f': Okay, we{punc}ll call it a draw. Come, Pasty! (')}{answer_king_queen} {player} {Y(f'{punc}rides{punc} away)')}\n{knight}{Y(f': (calling after them) Oh! Had enough, eh? Come back and take what{punc}s coming to you, you yellow bastards!! Come back here and take what{punc}s coming to you! I{punc}ll bite your legs off!')}")
        return limbs_left


def print_player_blocks(player_shield_blocks, random_attack, answer_king_queen, black_knight_limbs, player, Y, knight, punc):

    if player_shield_blocks == 2 and black_knight_limbs > 2:
        blocks_left = print(
            f"\n{Y('The')} {knight} {Y(f'dodges {answer_king_queen} {player}')}{Y(f'{punc}')}{Y(f's strike, and hurls his {random_attack}')} {Y(f'hand at {answer_king_queen} {player}')}{Y('.')}\n\n{answer_king_queen} {player} {Y(f'blocks the {knight}')}{Y(f'{punc}')}{Y(f's {random_attack} ')}{Y(f'but remains unscathed!')}\n\n{answer_king_queen} {player}{Y(f': Aha! You are as weak as I thought!')}\n{knight}{Y(f': None before have passed! You')}{Y(f'{punc}ll see!')}\n")
        return blocks_left
    elif player_shield_blocks == 2 and black_knight_limbs <= 2:
        blocks_left = print(
            f"\n{Y('Surpisingly fast for having no arms, the')} {knight} {Y(f'dodges {answer_king_queen} {player}')}{Y(f'{punc}')}{Y(f's strike, and kicks his {random_attack}')} {Y(f'foot at {answer_king_queen} {player}')}{Y('.')}\n\n{answer_king_queen} {player} {Y(f'blocks the {knight}')}{Y(f'{punc}')}{Y(f's {random_attack} ')}{Y(f'but remains unscathed!')}\n\n{answer_king_queen} {player}{Y(f': Aha! You are as weak as I thought!')}\n{knight}{Y(f': None before have passed! You')}{Y(f'{punc}ll see!')}\n")
        return blocks_left
    elif player_shield_blocks == 1 and black_knight_limbs > 2:
        blocks_left = print(
            f"\n{Y('Once again the')} {knight} {Y(f'dodges {answer_king_queen} {player}')}{Y(f'{punc}')}{Y(f's strike, and catapult{punc}')}{Y(f's his {random_attack}')} {Y(f'hand at {player}')}{Y('.')}\n\n{answer_king_queen} {player} {Y(f'barely blocks the {knight}')}{Y(f'{punc}')}{Y(f's {random_attack} ')}{Y(f'and stumbles backwards from the blow!')}\n\n{answer_king_queen} {player}{Y(f': That was a close one sir knight! But I am a')} {answer_king_queen}{Y(f', do you think I would be so easily conquered?')}\n{knight}{Y(f': You will soon fall to the fearless {knight}')}{Y('!')}\n")
        return blocks_left
    elif player_shield_blocks == 1 and black_knight_limbs > 2:
        blocks_left = print(
            f"\n{Y('Once again the')} {knight} {Y(f'dodges {answer_king_queen} {player}')}{Y(f'{punc}')}{Y(f's strike, and super kicks his {random_attack}')} {Y(f'foot at {answer_king_queen} {player}')}{Y('.')}\n\n{answer_king_queen} {player} {Y(f'barely blocks the {knight}')}{Y(f'{punc}')}{Y(f's {random_attack} ')}{Y(f'and stumbles backwards from the blow!')}\n\n{answer_king_queen} {player}{Y(f': That was a close one sir knight! But I am a')} {answer_king_queen}{Y(f', do you think I would be so easily conquered?')}\n{knight}{Y(f': You will soon fall to the legless {knight}')}{Y('!')}\n")
        return blocks_left
    elif player_shield_blocks == 0 and black_knight_limbs > 2:
        blocks_left = print(
            f"\n{Y('The')} {knight} {Y(f'dances around {answer_king_queen} {player}')}{Y(f'{punc}')}{Y(f's strike, and strikes {answer_king_queen} {player}')} {Y(f'with his {random_attack}')} {Y(f'hand.')} {answer_king_queen} {player} {Y(f'blocks the {random_attack}')} {Y(f'and is knocked over onto the ground, destroying the {answer_king_queen}')}{Y(f'{punc}')}{Y('s shield in the process.')}\n\n{answer_king_queen} {player}{Y(f': (getting up) I suggest you enjoy this moment while it lasts, because this will be your last!')}\n{knight}{Y(f': What happened? Is {player}')}{Y(f', noble {answer_king_queen}')} {Y('of the Britons')} {Y(f'scared now?!')}\n{answer_king_queen} {player}{Y(f': You{punc}')}{Y('ll pay for mocking the throne!')}\n")
        return blocks_left
    elif player_shield_blocks == 0 and black_knight_limbs <= 2:
        blocks_left = print(
            f"\n{Y('The')} {knight} {Y(f'dances around {answer_king_queen} {player}')}{Y(f'{punc}')}{Y(f's strike, and jump kicks {answer_king_queen} {player}')} {Y(f'with his {random_attack}')} {Y(f'foot.')}\n\n{answer_king_queen} {player} {Y(f' blocks the {random_attack}')} {Y(f', but is knocked over onto the ground, destroying the {answer_king_queen}')}{Y(f'{punc}')}{Y('s shield in the process')}\n\n{answer_king_queen} {player}{Y(f': (getting up) I suggest you enjoy this moment while it lasts, because this will be your last!')}\n{knight}{Y(f'What happened? Is {player}')}{Y(f', noble {answer_king_queen}')}{Y('of the Britons')} {Y(f'scared now?!')}\n{answer_king_queen} {player}{Y(f': You{punc}')}{Y('ll pay for mocking the throne! Just you wait!')}\n")
        return blocks_left
    elif player_shield_blocks == -1 and black_knight_limbs <= 2:
        blocks_left = print(
            f"\nI am dead! knight has arms")
        return blocks_left
    elif player_shield_blocks == -1 and black_knight_limbs <= 2:
        blocks_left = print(
            f"\nI am dead! knight has no arms")
        return blocks_left


def print_game_instructions(rock, paper, scissors, flesh, you, knight, Y):
    print(f"\n\n{Y('Welcome to')} {rock}{Y(',')} {paper}{Y(',')} {scissors}{Y(',')} {flesh}{Y('.')}\n\n      {crayons.yellow(f'In this game {you}')} {Y(f'will be playing against the {knight}')} {Y('from Monty Python and the Holy Grail.')}\n      {crayons.yellow(f'The goal is to to beat the {knight}')} {Y('and cross the bridge by choosing 1 of the 4 options available:')}\n\n{rock}{Y(':')}\n   {Y('Wins against')} {scissors}\n   {Y('Loses against')} {paper}\n\n{paper}{Y(':')}\n   {Y('Wins against')} {rock}\n   {Y('Loses against')} {scissors}\n\n{scissors}{Y(':')}\n   {Y('Wins against')} {paper}\n   {Y('Loses against')} {rock}\n\n{flesh}{Y(':')}\n   {Y('You will see...')}\n\n\n")


def print_game_start(answer_king_queen, player, punc, one, Y, Exit):
    print(f"\n{Y('Okay')} {answer_king_queen} {player}{Y(f', Let{punc}s go ahead and start the adventure!')}\n\n{Y('Please enter:')}\n   {Y(f'{punc}{one}')}{Y(f'{punc} to grab your coconuts and gallop away!')}\n   {Y(f'{punc}{Exit}')}{Y(f'{punc} to end your journey.')}")


def print_game_start_repeat(punc, one, Exit, R):
    print(
        f"\n{R(f'Please enter: {punc}{one}')}{R(f'{punc} or {punc}{Exit}')}{R(f'{punc}.')}")


def print_choose_attack(rock, paper, scissors, flesh, Y):
    print(
        f"\n{Y('Choose your attack: ')}{Y(f'{rock}')}{Y(',')} {Y(f'{paper}')}{Y(',')} {Y(f'{scissors}')}{Y(',')} {Y(f'{flesh}')}{Y('.')}")


def print_choose_attack_repeat(rock, paper, scissors, flesh, R, punc):
    print(f"\n{R('Please enter:')} {R(f'{punc}{rock}')}{R(f'{punc}')}{R(',')} {R(f'{punc}{paper}')}{R(f'{punc}')}{R(',')} {R(f'{punc}{scissors}')}{R(f'{punc}')}{R(', or')} {R(f'{punc}{flesh}')}{R(f'{punc}')}{R('.')}")


def print_clop_journey_starts(knight, player, answer_king_queen, Y, punc):
    print(
        f"\n\n\n{Y('(clop clop clop)')}\n\n{Y('(clop clop clop)')}\n\n{Y('(clop clop clop)')}\n\n{answer_king_queen} {player} {Y(f'and his trusty servant Patsy {punc}ride{punc} along through the woods. Suddenly they come apon a stream crossing where two knights are battling in a heated duel with giant longswords. One is dressed in green and one in black.')} {answer_king_queen} {player} {Y(f'stops and watches the fight. The two knights attempt to maul each other in many various ways and with many different tools of medieval weaponry. Finally, when the green knight is charging the black with a battle axe, the')} {knight} {Y(f'throws his sword straight through the slit in the green knight{punc}s helmet. The green knight falls to the ground, bleeding profusely. The')} {knight} {Y(f'steps forward and pulls his sword out of the helmet.')} {answer_king_queen} {player}{Y(f', impressed with the')} {knight}{Y(f'{punc}s fighting, motions to Patsy and they {punc}ride{punc} forward.')}\n\n{Y(f'{knight}')}{Y(': NONE SHALL PASS.')}\n{answer_king_queen} {player}{Y(': (taken aback) What?')}\n{Y(f'{knight}')}{Y(': NONE SHALL PASS.')}\n{answer_king_queen} {player}{Y(': I have no quarrel with you, good sir knight, but I must cross this bridge.')}\n{Y(f'{knight}')}{Y(': THEN YOU SHALL DIE.')}\n{answer_king_queen} {player}{Y(f': I *command* you, as {answer_king_queen}')}{Y(' of the Britons, to stand aside.')}\n{Y(f'{knight}')}{Y(f': I MOVE FOR NO {answer_king_queen.upper()}')}{Y('.')}\n{answer_king_queen} {player}{Y(': So be it!   (draws hand and shield)')}")


def player_attack_input(attack, answer_king_queen, player, knight, random_attack, rock, paper, scissors, Y, flesh, punc, R):
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
        while (attack != "Exit"):
            print(
                f"{Y('    Please choose the first attack you would like to perform:')}")
            flesh_1 = input("    ").capitalize()
            if flesh_1 != "Rock" and flesh_1 != "Paper" and flesh_1 != "Scissors":
                print(f"\n{R('Please enter:')} {R(f'{punc}{rock}')}{R(f'{punc}')}{R(',')} {R(f'{punc}{paper}')}{R(f'{punc}')}{R(', or')} {R(f'{punc}{scissors}')}{R(f'{punc}')}")
            elif flesh_1 == "Rock":
                pick_one = rock
                break
            elif flesh_1 == "Paper":
                pick_one = paper
                break
            elif flesh_1 == "Scissors":
                pick_one = scissors
                break

        while (attack != "Exit"):
            print(
                f"{Y('    Please choose the second attack you would like to perform:')}")
            flesh_2 = input("    ").capitalize()

            if flesh_2 != "Rock" and flesh_2 != "Paper" and flesh_2 != "Scissors" or flesh_1 == flesh_2:
                print(f"\n{R('Please enter:')} {R(f'{punc}{rock}')}{R(f'{punc}')}{R(',')} {R(f'{punc}{paper}')}{R(f'{punc}')}{R(', or')} {R(f'{punc}{scissors}')}{R(f'{punc}')}\n{R(f'      <Both choices can{punc}t be the same>')}")
            elif flesh_2 == "Rock":
                pick_two = rock
                break
            elif flesh_2 == "Paper":
                pick_two = paper
                break
            elif flesh_2 == "Scissors":
                pick_two = scissors
                break

        flesh_attack = (f"{flesh_1}/{flesh_2}")

        print(f"\n{answer_king_queen} {player} {Y(f'strikes the {knight}')}{Y(' with a')} {flesh}{Y(f'({pick_one}')}{Y(f'/')}{Y(f'({pick_two}')}{Y(f')... the {knight}')} {Y(f'simultaneously strikes back with his {random_attack}')}")
        return flesh_attack


def flesh_wound_win_lose(random_attack, rock, paper, scissors, answer_king_queen, player, flesh, punc, Y, knight, attack, black_knight_limbs, player_shield_blocks):
    if (random_attack == (f"{paper}") and (attack == "Rock/Paper" or attack == "Paper/Rock")) or (random_attack == (f"{rock}") and (attack == "Rock/Scissors" or attack == "Scissors/Rock")) or (random_attack == (f"{scissors}") and (attack == "Scissors/Paper" or attack == "Paper/Scissors")):
        black_knight_limbs += 1
        player_shield_blocks -= 1
        attack = flesh
        print_player_blocks(
            player_shield_blocks, random_attack, answer_king_queen, black_knight_limbs, player, Y, knight, punc)
        print(
            f"\n{Y(f'Wow! {answer_king_queen} {player}')} {Y(f'... Even with a {flesh}')}{Y(f' you managed to lose a round to the {knight}')}")
        print(
            f"{knight}{Y(': gains 1 limb back')}\n{answer_king_queen} {player}{Y(f': loses one block')}")
    elif (random_attack == (f"{paper}") and (attack == "Scissors/Paper" or attack == "Scissors/Rock" or attack == "Rock/Scissors" or attack == "Paper/Scissors")) or (random_attack == (f"{rock}") and (attack == "Paper/Scissors" or attack == "Paper/Rock" or attack == "Scissors/Paper" or attack == "Rock/Paper")) or (random_attack == (f"{scissors}") and (attack == "Rock/Paper" or attack == "Rock/Scissors" or attack == "Paper/Rock" or attack == "Scissors/Rock")):

        black_knight_limbs -= 1
        attack = flesh
        print_black_knight_dismember(
            black_knight_limbs, attack, random_attack, player, Y, punc, knight, answer_king_queen)
        print(
            f"\n\n{Y(f'Don{punc}t feel too proud of yourself, {answer_king_queen} {player}')}{Y(f'... You had to use a {flesh}')}{Y(f' to get the job done.')}")
    return black_knight_limbs, player_shield_blocks


def normal_attack_win_lose(random_attack, scissors, attack, answer_king_queen, knight, punc, player, black_knight_limbs, player_shield_blocks, rock, paper, Y):
    if (random_attack == (f"{scissors}") and attack == rock) or (random_attack == (f"{rock}") and attack == paper) or (random_attack == (f"{paper}") and attack == scissors):
        black_knight_limbs -= 1
        print_black_knight_dismember(
            black_knight_limbs, attack, random_attack, player, Y, punc, knight, answer_king_queen)
    elif (random_attack == (f"{paper}") and attack == rock) or (random_attack == (f"{scissors}") and attack == paper) or (random_attack == (f"{rock}") and attack == scissors):
        player_shield_blocks -= 1
        print_player_blocks(
            player_shield_blocks, random_attack, answer_king_queen, black_knight_limbs, player, Y, knight, punc)
    elif (random_attack == (f"{rock}") and attack == rock) or (random_attack == (f"{paper}") and attack == paper) or (random_attack == (f"{scissors}") and attack == scissors):
        print_tie(Y, knight)
    return black_knight_limbs, player_shield_blocks


def main():
    input1 = ""
    rock = crayons.blue('Rock')
    paper = crayons.green('Paper')
    scissors = crayons.black('Scissors')
    flesh = crayons.red('Flesh Wound')
    Y = crayons.yellow
    R = crayons.red
    knight = crayons.magenta('Black Knight')
    you = crayons.cyan('you')
    one = crayons.cyan('1')
    Exit = crayons.cyan('Exit')
    punc = "'"
    black_knight_limbs = 4
    player_shield_blocks = 3

    while input1 != "Exit":
        print_game_instructions(rock, paper, scissors, flesh, you, knight, Y)
        player = pick_name(Y)
        answer_king_queen = pick_king_queen(Y, punc, R)
        print_game_start(answer_king_queen, player, punc, one, Y, Exit)

        while (input1 != 1 or input1 != "Exit"):
            input1 = input("    ")
            input2 = ""
            if input1.isdigit():
                input2 = int(input1)
            elif input1.capitalize() == "Exit":
                print_exit_game(Y, punc)
                quit()
            if input2 == 1:
                print_clop_journey_starts(
                    knight, player, answer_king_queen, Y, punc)
                break
            else:
                print_game_start_repeat(punc, one, Exit, R)

        while (input1 != "Exit"):
            if player_shield_blocks < 0 or black_knight_limbs == 0:
                break
            print_choose_attack(rock, paper, scissors, flesh, Y)
            print_remaining_lives_block(
                black_knight_limbs, player_shield_blocks, player, knight, Y, answer_king_queen)
            attack = input("    ").capitalize()
            random_attack = cpu_random_attack(rock, paper, scissors)
            print_commence_battle(
                player_shield_blocks, black_knight_limbs, player, Y, random_attack, attack, knight)

            if attack != "Rock" and attack != "Paper" and attack != "Scissors" and attack != "Flesh wound":
                print_choose_attack_repeat(
                    rock, paper, scissors, flesh, R, punc)

            attack = player_attack_input(
                attack, answer_king_queen, player, knight, random_attack, rock, paper, scissors, Y, flesh, punc, R)

            normal_new_limb_block = normal_attack_win_lose(
                random_attack, scissors, attack, answer_king_queen, knight, punc, player, black_knight_limbs, player_shield_blocks, rock, paper, Y)

            black_knight_limbs = normal_new_limb_block[0]
            player_shield_blocks = normal_new_limb_block[1]

            flesh_wound_new_limb_block = flesh_wound_win_lose(
                random_attack, rock, paper, scissors, answer_king_queen, player, flesh, punc, Y, knight, attack, black_knight_limbs, player_shield_blocks)

            black_knight_limbs = flesh_wound_new_limb_block[0]
            player_shield_blocks = flesh_wound_new_limb_block[1]
        break


if __name__ == "__main__":
    main()

# TODO add new message when knight gains lives and loses them as well
