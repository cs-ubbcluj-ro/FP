import random
from domain import Sentince

class Services:
    def __init__(self, repo):
        self.__repo = repo 
        self.__sentince = None
        self.__lives = 6
        self.pick_random_sentince()
        self.reveal_initial_data()
        pass 
    
    def letter_exists(self, char):
        return char in self.__sentince
                
    def split_into_words(self):
        return self.__sentince.split_into_words()
    
    def reveal_all_occurences(self, char):
        self.__sentince.reveal_all_occurences(char)
        
    def reveal_initial_data(self):
        split_sentince = self.split_into_words()
        for word in split_sentince:
            if word.isalpha():
                self.__sentince.reveal_all_occurences(word[0])
                self.__sentince.reveal_all_occurences(word[-1])
                
    def is_game_won(self):
        return self.__sentince.is_complete()
    
    def is_game_lost(self):
        return self.__lives == 0
    
    def is_game_over(self):
        return self.is_game_won() or self.is_game_lost()
    
    def get_sentince(self):
        return self.__sentince
    
    def check_letter(self, letter):
        if self.letter_exists(letter):
            self.reveal_all_occurences(letter)
        else:   
            self.__lives -= 1
            
    def pick_random_sentince(self):
        sentince = random.choice(self.__repo.get_sentinces())
        self.__sentince = Sentince(sentince)
        
    def add_sentince(self, sentince):
        self.__repo.add_sentince(sentince)
        
    def get_lives(self):
        return self.__lives