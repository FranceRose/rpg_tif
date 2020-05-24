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
	choice = int(input("Pierre [0], Papier [1], Ciseaux [2]?"))
	choice_lisa = random.randint(0, 2)
	choice_raphael = random.randint(0, 2)
	m_ = max(config.shifumi_truth_table[choice][choice_lisa], config.shifumi_truth_table[choice][choice_raphael])
	while m_ == -1:
		# ex-aequo
		choice = int(input("Ax-aequo.\nPierre [0], Papier [1], Ciseaux [2]?"))
		choice_lisa = random.randint(0, 2)
		choice_raphael = random.randint(0, 2)
		m_ = max(config.shifumi_truth_table[choice][choice_lisa], config.shifumi_truth_table[choice][choice_raphael])

	if m_ == 0:
		# Tif looses
		print('Tu as perdu !')
		return False
	print('Tu as gagne !')
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
