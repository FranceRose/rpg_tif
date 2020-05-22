# RPG USEFUL FUNCTIONS
import random
import math
import rpg_config as config

def get_time_in_hours(time, end=22, print_bool=True):
	#TODO: fix the case with print_bool
	if print_bool:
		return (end - time//60, time % 60)
	return end - time / 60


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



menu_choice = {0: "Faire amener un hamac pour piéger Daoult [Obligatoire] (temps estimé: 15mn)", 
			   1: "Diplôme de thèse [Obligatoire] (temps estimé: 1h sans alexis, 15mn avec Alexis) Réaliser avant 18h. Impossible de réaliser entre 12h et 14h sauf si Alexis est présent.",
               2: "Organiser un tournoi de babyfoot [Obligatoire] (temps estimé: 1h)",
	           3: "Manger [Facultatif] (20 mn) (possible jusque 15h)",
			   4: "Sieste"}

def display_menu(time, hamac, diploma, babyfoot, eaten):
	to_display = dict(menu_choice)
	if hamac:
		del to_display[0]
	if diploma:
		del to_display[1]
	elif get_time_in_hours(time, print_bool=False) > config.diploma_deadaline:
		del to_display[1]
	if babyfoot:
		del to_display[2]
	if eaten:
		del to_display[3]
	elif get_time_in_hours(time, print_bool=False) > config.lunch_deadline:
		del to_display[3]
	return to_display

