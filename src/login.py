from utils.hash import hash_password
from time import sleep
from utils.colors import bcolors as bc

def login(users:dict) -> str:
    username = input("Username: ")
    password = hash_password(input("Senha: "))
    user = users.get(username)
    if username not in users:
        print(f"{bc.WARNING}O usuário {username} não foi encontrado!\nTente novamente.{bc.ENDC}")
        sleep(2)
        return None
    if users[username].password != password:
        print(f"{bc.FAIL}Senha inválida!\nTente novamente.{bc.ENDC}")
        sleep(2)
        return None
    return user
