# MAIN SCRIPT RPG TIF
import sys
import rpg_config as config
from rpg_functools import *
import random

from os import system, name

def credits():
    clear_screen()
    input("A faire")

def launch_video():
    open_file('./narration/rise_of_champetier.mp4')
    clear_screen()

def menu_principal():
    while(True):
        menu_choice = check_input(p_color('narration/menu_principal.txt'),['1','2','3','4'])
        if menu_choice == "1":
            launch_video()
        if menu_choice == "2":
            clear_screen()
            game()
        if menu_choice == "3":
            credits()
        if menu_choice == "4":
            exit(0)
        clear_screen()



def die():
    clear_screen()
    print(p_color("[RED]CATASTROPHE ! \n[GREEN]Tiphaine[DEFAULT] a [RED]crevé[DEFAULT]. Elle a visiblement fait de très [RED]mauvais[DEFAULT] choix... Il faut recommencer"),file=False)
    menu_principal()

hamac_votes = []

# global variables
time = config.start_hour * 60 # 16 hours
energy = Energy(100)

# France & Guillaume encounters
discuss_france = check_input(p_color("narration/convaincre_le_monde/discussion_france_beginning.txt"),
							 ['T', 'F'])
if discuss_france == 'T':
	print(p_color("narration/convaincre_le_monde/discussion_france_follow.txt"))
	print_result_action(config.france_dt, config.france_e - energy.e)

	time += config.france_dt
	energy += config.france_e
	huel = True
	hamac_votes.append('france')

print_INFO(time, energy)
input()
clear_screen()


discuss_guillaume = check_input(p_color("narration/convaincre_le_monde/choice_discussion_guillaume.txt"),
								['T', 'F'])
if discuss_guillaume == 'T':
	time += config.guillaume_dt
	energy += config.guillaume_de
	hamac_votes.append('guillaume')

	print(p_color("narration/convaincre_le_monde/discussion_guillaume.txt"))
	print_result_action(config.guillaume_dt, config.guillaume_de)

if DEBUG:
	print('\nF&G ENCOUNTERS')
	print(f'hamac_votes = {hamac_votes}')
