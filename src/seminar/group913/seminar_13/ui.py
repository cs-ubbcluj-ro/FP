from services import Services
from domain import Hangman

class UI:
    def __init__(self, services):
        self.__services = services
        pass 
    
    def print_main_menu(self):
        print("1. Start game")
        print("2. Add a sentince")
        print("0. Exit")
    
    def run_main_menu(self):
        commands = {
            "1": self.run_game,
            "2": self.add_sentince
        }
        
        while True:
            self.print_main_menu()
            command = input(">>> ")
            try:
                if command == "0":
                    return
                elif command == "1":
                    self.run_game()
                    break
                if command == "2":
                    self.add_sentince()
                else:
                    print("Invalid command")
            except ValueError as ve:
                print(ve)
    
    def read_letter(self):
        letter = input("Guess a letter: ")
        if len(letter) != 1 or not letter.islower():
            print("Invalid input")
            self.read_letter()
            return 
        
        self.__services.check_letter(letter)
            
    def check_gameover(self):
        if self.__services.is_game_over():
            if self.__services.is_game_won():
                print("You won!")
            else:
                print("You lost!")
            return True
    
    def print_sentince(self):
        print(str(self.__services.get_sentince()))
        
    def run_game(self):
        while True:
            self.print_sentince()
            self.print_hangman()
            self.read_letter()
            if self.check_gameover():
                break               
    
    def add_sentince(self):
        sentince = input("Enter sentince: ")
        words = sentince.split()
        if len(words) < 1 or any([len(word) < 3 for word in words]):
            print("Invalid sentince")
            self.add_sentince()
            return
        self.__services.add_sentince(sentince)
        print("sentince added succesfully")
        
    def print_hangman(self):
        lives = self.__services.get_lives()
        hangman = Hangman(lives)
        print(str(hangman))