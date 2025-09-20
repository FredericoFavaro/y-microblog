from datetime import datetime

class Post:
    def __init__(self, author, content):
        self.author = author
        self.content = content
        self.timestamp = datetime.now().strftime('%d/%m/%Y %H:%M')

    def __str__(self):
        return f"{self.author} ({self.timestamp})\n{self.content}"


class User:
    def __init__(self, username, realname, email, password):
        self.username = username
        self.realname = realname
        self.email = email
        self.password = password
        self.posts = []

    def post_content(self, content):
        content = Post(self.username, content)
        self.posts.append(content)
        print(content)
        return content
