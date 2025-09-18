from datetime import datetime

class Post:
    def __init__(self, author, msg):
        self.author = author
        self.msg = msg
        self.timestamp = datetime.now().strftime('%d/%m/%Y %H:%M')

    def __str__(self):
        return f"{self.author} ({self.timestamp})\n{self.msg}"

    def __repr__(self):...

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password
        self.posts = []

        def post_content(self, content):
            content = Post(self, content)
            self.posts.append(content)
            return content






