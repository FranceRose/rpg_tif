from rpg_functools import time2hours


def clear():
    if name == 'nt':
        _ = system('cls')

    else:
        _ = system('clear')


class bcolors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    DEFAULT = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def p_color(input):  # Afficher avec une couleur
    if type(input) != str:
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
    print(p_color(f"Il est [BOLD]{time2hours(time)}[DEFAULT]. Il te reste [BOLD][YELLOW]{energy} d'energie."))
    return
