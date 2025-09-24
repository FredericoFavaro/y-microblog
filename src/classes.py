from datetime import datetime
from utils.colors import bcolors as bc

def hit_continue():
    input("Aperte qualquer tecla para continuar.")

class Post:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.timestamp = datetime.now().strftime('%d/%m/%Y %H:%M')

    def __str__(self):
        return f"{bc.BOLD}{self.author} ({self.timestamp}){bc.ENDC}\n{self.content}"


class User:
    def __init__(self, username, realname, email, password):
        self.username = username
        self.realname = realname
        self.email = email
        self.password = password
        self.following = []
        self.posts = []

    def __str__(self):
        return f"Usuário: {self.username}\nNome: {self.realname}\nE-mail: {self.email}\nSeguindo: {self.following}"
    
    def post_content(self, content):
        content = Post(self.username, content)
        self.posts.append(content)
        print(content)
        return content
    
    def show_posts(self):
        if not self.posts:
            print("Você não postou nada ainda.")
            hit_continue()
            return
        for post in self.posts:
            print(post)

    def follow_user(self, user):
        if user not in self.following:
            self.following.append(user)
