from utils.hash import hash_password

def login(users:dict) -> str:
    username = input("Username: ")
    password = hash_password(input("Senha: "))
    user = users.get(username)
    print(user)
    if username not in users:
        print(f"O usuário {username} não foi encontrado")
        return False
    if users[username].password == password:
        return True
    return None
