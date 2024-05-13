import os

class UserManager:
    def __init__(self):
        self.users = {}
        self.current_user = None
        self.load_users()

    def load_users(self):
        if not os.path.exists("data"):
            os.makedirs("data")
        if not os.path.exists("data/users.txt"):
            with open("data/users.txt", "w"):
                pass
        else:
            with open("data/users.txt", "r") as file:
                for line in file:
                    username, password = line.strip().split(",")
                    self.users[username] = password

    def save_users(self):
        with open("data/users.txt", "w") as file:
            for username, password in self.users.items():
                file.write(f"{username},{password}\n")

    def validate_username(self, username):
        if len(username) < 4:
            return False
        return True

    def validate_password(self, password):
        if len(password) < 8:
            return False
        return True

    def register(self, username, password):
        if username in self.users:
            print("\n******************************************************")
            print("Username already exists. Please choose a different one.")
            print("*******************************************************")
            return True
        if not self.validate_username(username):
            print("\n*************************************************")
            print("\nUsername must be at least 4 characters long.")
            print("************************************************")
            return True
        if not self.validate_password(password):
            print("\n*************************************************")
            print("\n1Password must be at least 8 characters long.")
            print("************************************************")
            return True
        
        self.users[username] = password
        self.save_users()
        print("\n+++++Registration successful!+++++")
        return True

    def login(self, username, password):
        if username in self.users and self.users[username] == password:
            self.current_user = username
            return True, self.current_user
        else:
            return False

	