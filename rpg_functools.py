# RPG USEFUL FUNCTIONS
import random
import math
import rpg_config as config

def check_input(txt, choices):
	key = input(txt)
	key = key.upper()
	while key not in choices:
		print(f"Ta réponse n'est pas reconnue. [{'/'.join(choices)}]")
		key = input()
	return key


def time2hours(time):
	return f"{time//60}h{time%60:02d}"

def shifumi():
	choice = int(check_input(p_color("narration/gpu/shifumi_play.txt"),
							 ['0', '1', '2']))
	choice_lisa = random.randint(0, 2)
	choice_raphael = random.randint(0, 2)
	m_ = max(config.shifumi_truth_table[choice][choice_lisa],
			 config.shifumi_truth_table[choice][choice_raphael])

	while m_ == -1:
		# ex-aequo
		print("Ex-aequo.")
		choice = int(check_input(p_color("narration/gpu/shifumi_play.txt"),
								 ['0', '1', '2']))
		choice_lisa = random.randint(0, 2)
		choice_raphael = random.randint(0, 2)
		m_ = max(config.shifumi_truth_table[choice][choice_lisa],
				 config.shifumi_truth_table[choice][choice_raphael])

	if m_ == 0:
		# Tif looses
		print(p_color("narration/gpu/shifumi_loose.txt"))
		return False

	print(p_color("narration/gpu/shifumi_win.txt"))
	return True


menu_choice = {0: "Faire amener un hamac pour piéger Daoult [Obligatoire]",
			   1: "Diplôme de thèse [Obligatoire] Réaliser avant 18h.",
               2: "Organiser un tournoi de babyfoot [Obligatoire]",
	           3: "Manger [Facultatif] Possible jusque 15h.",
			   4: "Sieste [Facultatif]"}

def display_menu(time, hamac, diploma, babyfoot, eaten):
	to_display = dict(menu_choice)
	if hamac:
		del to_display[0]
	if diploma:
		del to_display[1]
	elif time > config.diploma_deadline * 60:
		del to_display[1]
	if babyfoot:
		del to_display[2]
	if eaten:
		del to_display[3]
	elif time > config.lunch_deadline * 60:
		del to_display[3]
	return to_display


def daoult_attack(covid, hamac, fungus):
	to_display = {0: "covid",
				  1: "hamac",
				  2: "champignon"}
	if not covid:
		del to_display[0]
	if not hamac:
		del to_display[1]
	if not fungus:
		del to_display[2]
	txt = "Tu attaques Daoult avec le " + ','.join([f'{value} [{key}]' for key, value in to_display.items()])
	return txt

def clear_screen():
    # if name == 'nt':
    #     _ = system('cls')
    #
    # else:
    #     _ = system('clear')
    pass


class bbcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    DEFAULT = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def p_color(input, file=True):  # Afficher avec une couleur
    if file:
        input = open(input, 'r').read()
    string = input.replace("[BLUE]", bbcolors.BLUE) \
        .replace("[GREEN]", bbcolors.GREEN) \
        .replace("[YELLOW]", bbcolors.YELLOW) \
        .replace("[RED]", bbcolors.RED) \
        .replace("[DEFAULT]", bbcolors.DEFAULT) \
        .replace("[BOLD]", bbcolors.BOLD) \
        .replace("[UNDERLINE]", bbcolors.UNDERLINE)
    return string


def print_INFO(time, energy):
    print('*'*80)
    print('** ', end='          ')
    print(p_color(f"Il est [GREEN][BOLD]{time2hours(time)}[DEFAULT]. Il te reste [BOLD][YELLOW]{energy} d'#NRJ[DEFAULT].",
                  file=False))
    print('*' * 80)
    return

def print_result_action(dt, de):
    txt = f"Cette action t'a pris [GREEN][BOLD]{dt} minutes[DEFAULT] et "
    if de > 0:
        txt += "tu as gagné "
    else:
        txt += "tu as perdu "
    txt += f"[YELLOW][BOLD]{de} point(s) d'#NRJ[DEFAULT]."

    print('*' * 80)
    print('** ', end='          ')
    print(p_color(txt, file=False))
    print('*' * 80)
    return
