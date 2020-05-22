# RPG USEFUL FUNCTIONS
import random
import rpg_config as config

def get_time_in_hours(time, start=8, print_bool=True):
	hours_since_start = time // 60
	leftover_minutes = time % 60
	if print_bool:
		return (start+hours_since_start, leftover_minutes)
	return start + time/60


def shifumi():
	choice = int(input("Pierre [0], Papier [1], Ciseaux [2]?"))
	choice_lisa = random.randint(0, 2)
	choice_raphael = random.randint(0, 2)
	m_ = min(config.shifumi_truth_table[choice][choice_lisa], config.shifumi_truth_table[choice][choice_raphael])
	while m_ == -1:
		# ex-aequo
		choice = int(input("Ax-aequo.\nPierre [0], Papier [1], Ciseaux [2]?"))
		choice_lisa = random.randint(0, 2)
		choice_raphael = random.randint(0, 2)
		m_ = min(config.shifumi_truth_table[choice][choice_lisa], config.shifumi_truth_table[choice][choice_raphael])

	if m_ == 0:
		# Tif looses
		print('Tu as perdu !')
		return False
	print('Tu as gagne !')
	return True