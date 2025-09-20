from utils.title import title
from login import login
from classes import User, Post
from user_register import user_register
from utils.menu import menu_inicial
from time import sleep
from utils.clean_screen import limpar_tela


users = {}
users["Fred"] = User("Fred", "Frederico", "fred@gmail.com", "03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4")

current_user = None

while True:
    title()
    menu_inicial()
    opcao = input(">>>  ")
    match opcao:
        case "1":
            current_user = login(users)
            if current_user:
                ...
                # Abrir menu
        case "2":
            user_register(users)
        case "x"|"X":
            limpar_tela()
            print()
            print("Fechando o Y...")
            sleep(1)
            limpar_tela()
            exit()
        case _:
            print("valor informado não existe")