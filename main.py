# SANTIAGO, MARC STEPHEN R. CS-1202 ----- FINAL LAB EXAM ------ DICE ROLL GAME  
from utils.user_manager import UserManager
from utils.dice_game import DiceGame
from utils.score import Score
from utils.user import User
import sys

user_manager_inst = UserManager()
score_inst = Score()
user_inst = User()
dice_game = DiceGame(user_manager_inst, score_inst, user_inst)
current_user = user_manager_inst.current_user

while True:
    print("\n------------------")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    print("------------------\n")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        while True:
            username = input("Enter your username (at least 4 characters), or leave blank to cancel: ")
            if username == "" or username == " ":
                print("\n-------------CANCELLED-------------")
                break
            if not user_manager_inst.validate_username(username):
                print("\n*****Username must be at least 4 characters long.*****\n")
                break
            
            password = input("Enter your password (at least 8 characters), or leave blank to cancel: ")
            if password == "" or password == " ":
                print("\n-------------CANCELLED-------------")
                break
            if not user_manager_inst.validate_password(password):
                print("\n*****Password must be at least 8 characters long.*****")
                break
            
            if user_manager_inst.register(username, password):
                break

    elif choice == "2":
        print("\n-------------LOGIN-------------") 
        username = input("Enter username: ")
        if username == "" or username == " ":
            print("\n-------------CANCELLED-------------")
            break
        password = input("Enter password: ")
        if password == "" or password == " ":
            print("\n-------------CANCELLED-------------")
            break
        
        if user_manager_inst.login(username, password):
            current_user = user_manager_inst.current_user
            print(f"\n+++++++Login successful. Welcome, {current_user}!+++++++")
            dice_game.menu(current_user)         
        else:
            print("\n*****Invalid username or password. Please try again.*****")
        
    elif choice == "3":
        print("\n+++++++Exiting Game.+++++++")
        sys.exit() 
    else:
        print("\n-----Invalid option. Please input a valid number.-----")