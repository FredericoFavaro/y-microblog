from utils.clean_screen import limpar_tela
from utils.colors import bcolors as bc



def title():
    limpar_tela()
    print(rf""" {bc.OKCYAN}┓┏{bc.ENDC}
{bc.OKCYAN} ┗┫ {bc.ENDC}    A CLI Microblog
{bc.OKCYAN} ┗┛ {bc.ENDC}   Like X, but its {bc.OKCYAN}{bc.BOLD}Y{bc.ENDC}!
""")
