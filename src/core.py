from utils.title import title
from login import login
from classes import User, Post
from user_register import user_register
from utils.menu import menu_inicial, menu_principal
from time import sleep
from utils.clean_screen import limpar_tela
from user_data import users

current_user = None

def hit_continue():
    input("Aperte qualquer tecla para continuar.")

while True:
    title()
    print(current_user)
    menu_inicial()
    opcao = input(">>>  ")
    match opcao:
        case "1":
            current_user = login(users)
            print(current_user)
            if current_user:
                while True:
                    title()
                    print("")
                    print(f"Bem vindo, {current_user.username}!")
                    menu_principal()
                    opcao = input(">>> ")
                    match opcao:
                        case "1":
                            current_user.show_posts()
                            hit_continue()
                        case "2":
                            print(current_user)
                            hit_continue()
                        case "3":
                            content = input("Postagem: ")
                            current_user.post_content(content)
                            hit_continue()
                        case "4":
                            ...
                        case "0":
                            current_user = None
                            break
                        case "x":
                            limpar_tela()
                            print()
                            print("Fechando o Y...")
                            sleep(1)
                            limpar_tela()
                            exit()
                        case _:
                            print("valor informado não existe")
                            hit_continue()
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
            print("\nvalor informado não existe")
            hit_continue()

print(current_user)