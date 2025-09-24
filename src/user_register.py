from utils.hash import hash_password
from classes import User

def user_register(users):
    print("____________ Cadastro ____________\n")
    username = input("Nome de usuário: ")
    if username in users:
        print("Usuário já existe!")
        return
    realname = input("Nome real do usuário: ")
    email = input("Email do usuário: ")
    password = hash_password(input("Senha: "))
    
    users[username] = User(username, realname, email, password)
    print(users[username])