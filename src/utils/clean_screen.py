import os

def limpar_tela():
    try:
        if os.name == 'nt':
            os.system('cls')          # comando para limpar tela no terminal do windows
        else:
            os.system('clear')        # comando para limpar tela no linux e mac
    except:
        print("\033[H\033[J", end="") # limpa a tela usando códigos de escape ANSI,