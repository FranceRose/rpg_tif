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

def p_color(string): # Afficher avec une couleur
    class bbcolors:
        PURPLE = '\033[95m'
        BLUE = '\033[94m'
        GREEN = '\033[92m'
        YELLOW = '\033[93m'
        RED = '\033[91m'
        DEFAULT = '\033[0m'
        BOLD = '\033[1m'
        UNDERLINE = '\033[4m'
    string = string.replace("[BLUE]",bbcolors.BLUE).replace(
		"[GREEN]",bbcolors.GREEN).replace(
		"[YELLOW]",bbcolors.YELLOW).replace(
		"[RED]",bbcolors.RED).replace(
		"[DEFAULT]",bbcolors.DEFAULT).replace(
		"[BOLD]",bbcolors.BOLD).replace("[UNDERLINE]",bbcolors.UNDERLINE)
    print(f"{string}")

def print_INFO(life,time):
	print("")
