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
    menu_inicial()
    opcao = input(">>>  ")
    match opcao:
        case "1":   # Fazer login
            current_user = login(users)
            print(current_user)
            if current_user:
                while current_user != None:
                    title()
                    print("")
                    print(f"Bem vindo, {current_user.username}!")
                    menu_principal()
                    opcao = input(">>> ")
                    title()
                    match opcao:
                        case "1": # ver timeline
                            current_user.show_posts()
                            hit_continue()
                        case "2": # Ver perfil
                            print(current_user)
                            hit_continue()
                        case "3": # Postar conteudo
                            content = input("Postagem: ")
                            current_user.post_content(content)
                            hit_continue()
                        case "4": # Seguir usuário
                            user_to_follow = input("Nome do usuário que para seguir: ")
                            current_user.follow_user(user_to_follow)
                        case "0": # Desconectar
                            current_user = None
                        case "x": # Sair
                            title()
                            print("Você esta saindo!\nNos vemos mais tarde :)")
                            sleep(2)
                            limpar_tela()
                            exit()
                        case _:
                            print("valor informado não existe")
                            hit_continue()
        case "2":  # Cadastrar novo usuário
            title()
            user_register(users)
        case "x"|"X":  # Sair
            title()
            print("Você esta saindo!\nNos vemos mais tarde :)")
            sleep(2)
            limpar_tela()
            exit()
        case _:
            title()
            print("\nvalor informado não existe")
            hit_continue()

print(current_user)