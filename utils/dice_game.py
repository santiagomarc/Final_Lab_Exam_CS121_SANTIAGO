from .user_manager import UserManager
from .score import Score
from .user import User
import random
import string
import os


user_manager_inst = UserManager()
score_inst = Score()
user_inst = User()
current_user = user_manager_inst.current_user



class DiceGame:
    def __init__(self, user_manager_inst, score_inst, user_inst):
        self.user_manager_inst = user_manager_inst
        self.score_inst = score_inst
        self.user_inst = user_inst
        self.load_score()

    def load_score(self):
        if not os.path.exists("data"):
            os.makedirs("data")
            
        if not os.path.exists("data/rankings.txt"):
            with open("data/rankings.txt", "w"):
                pass
    def save_score(self, username, game_id, points, wins):
        self.score_inst = Score(username, game_id, points, wins)
        with open("data/rankings.txt", "a") as file:
            file.write(f"{username},{game_id},{points},{wins}\n")

    def play_game(self, current_user):
        user_wins = 0
        user_points = 0
        stage = 0
        
        while True:
            CPU_round_won = 0
            user_round_won = 0
            
            
            game_id = ''.join(random.choices(string.digits, k=4))
            with open("data/rankings.txt", "r") as file:
                for line in file:
                    if game_id in line:
                        game_id = ''.join(random.choices(string.digits, k=4))


            print(f"\n-------Starting game as {current_user}-------")
            for _ in range(3):
                
                print("\n++++++++++++++++++++++++++++++++++")
                user_rolls = random.randint(1, 6)
                CPU_rolls = random.randint(1, 6)
                
                print(f"{current_user} rolled {user_rolls}")
                print(f"CPU rolled {CPU_rolls}")

                if user_rolls == CPU_rolls:
                    print(f"It's a tie!")
                    print("++++++++++++++++++++++++++++++++++")
                elif user_rolls > CPU_rolls:
                    print(f"You won this round {current_user}")
                    print("++++++++++++++++++++++++++++++++++")
                    user_round_won += 1
                    user_points += 1
                else:
                    print(f"CPU wins this round!")
                    print("++++++++++++++++++++++++++++++++++")
                    CPU_round_won += 1
            
            if user_round_won == CPU_round_won:
                print(f"\n++++++++The stage is tie!+++++++++")
                print(f"         Additional roll!\n")
                while user_round_won == CPU_round_won:
                    user_rolls = random.randint(1, 6)
                    CPU_rolls = random.randint(1, 6)
                    print(f"{current_user} rolled {user_rolls}")
                    print(f"CPU rolled {CPU_rolls}")

                    if user_rolls == CPU_rolls:
                        print(f"\n---------It's a tie again!--------\n")
                        continue
                    elif user_rolls > CPU_rolls:
                        print(f"\n   You won the tie-breaker {current_user}!")
                        print("++++++++++++++++++++++++++++++++++")
                        user_round_won += 1
                        break
                    else:
                        print(f"\n-----CPU wins the tie-breaker!-----")
                        print("++++++++++++++++++++++++++++++++++")
                        CPU_round_won += 1
                        break
                
            if user_round_won >= 2:
                print(f"\n======You won this stage {current_user}!======")
                user_points += 3
                user_wins += 1
                print(f"\n{current_user}: Total points - {user_points}, Stages won: {user_wins}")
                  
                
                
                choice = input("Do you want to continue to the next stage? (1 = YES, 0 = NO): ")
                while choice not in ["0", "1"]:
                    choice = input("Invalid input. Please enter 1 to continue or 0 to stop: ")
                
                if choice == "1":
                    stage += 1
                    continue
                elif choice == "0":
                    stage += 1
                    print("\n-------The game has ended.-------")
                    self.save_score(current_user, game_id, user_points, user_wins) 
                    self.menu(current_user)
                    return
                
            elif CPU_round_won >= 2:
                print(f"\n-------You lost this stage {current_user}.-------")
                if stage == 0:
                    print(f"\n    Game over. You didn't win any stages.\n")
                elif stage >= 1:
                    print(f"\n    Game over. You reached {stage} stages.\n")
                print(f"{current_user}: Total points - {user_points}, Stages won: {user_wins}")
                self.save_score(current_user, game_id, user_points, user_wins)
                self.menu(current_user)
                return
            
    def show_top_scores(self, current_user):
        scores_list = []
        with open("data/rankings.txt") as file:
            print("\n                         TOP SCORES")
            print("*****************************************************************")
            for index in file:
                try:
                    username, game_id, points, wins = index.strip().split(",")
                    points = int(points)
                    scores_list.append((username, game_id, points, wins))
                except ValueError:
                    continue
        if scores_list == []:
            print("-------No games played yet. Play a game to see top scores!-------")
            self.menu(current_user)
        else:
            scores_list = sorted((scores_list), key=lambda x: x[2], reverse=True)[:10]
            for i, index in enumerate((scores_list), start = 1):
                print(f"{i}. {index[0]} --- Game ID #{index[1]} --- Points - {index[2]}, Wins: {index[3]}")
            print("*****************************************************************\n")
            self.menu(current_user)

    def logout(self, current_user):
        print(f"\n------User: {current_user} LOGGED OUT!------")
        current_user = None
        return

    def menu(self, current_user):
        print("\n-------------")
        print("1. Play Game")
        print("2. Show top scores")
        print("3. Logout")
        print("-------------\n")
        
        option = input("Enter your choice: ")
        
        if option == "1":
            self.play_game(current_user)
        elif option == "2":
            self.show_top_scores(current_user)
        elif option == "3":
            self.logout(current_user)
        else:
            print("\n*******Invalid option. Please try again.*******")
            self.menu(current_user)       

