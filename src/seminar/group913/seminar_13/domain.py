import random

class Sentince:
    def __init__(self, str):
        self.__str = str
        self.__is_charachter_revealed = [False] * len(self)
        
    def reveal_position(self, pos):
        self.__is_charachter_revealed[pos] = True
    
    def __getitem__(self, pos):
        return self.__str[pos]
    
    def __str__(self):
        formatted_str = ""
        for i in range(len(self)):
            if self.__str[i] == ' ' or self.__is_charachter_revealed[i]:
                formatted_str += self.__str[i]
            else:
                formatted_str += '_'
        return formatted_str

    def __len__(self):
        return len(self.__str)

    def is_complete(self):
        return all([self.__is_charachter_revealed[i] or self.__str[i] == ' ' for i in range(len(self))])
    
    def split_into_words(self):
        return self.__str.split()
    
    def reveal_all_occurences(self, char):
        for i in range(len(self.__str)):
            if self.__str[i] == char:
                self.reveal_position(i)

class Hangman:
    def __init__(self, lives):
        self.__lives = lives
        pass 
    
    def __str__(self):
        lives = self.__lives
        if lives == 0:
            return "  O  \n /|\\ \n / \\ "
        elif lives == 1:
            return "  O  \n /|\\ \n /  "
        elif lives == 2:
            return "  O  \n /|\\ \n    "
        elif lives == 3:
            return "  O  \n /|  \n    "
        elif lives == 4:
            return "  O  \n  |  \n    "
        elif lives == 5:
            return "  O  \n     \n    "
        elif lives == 6:
            return "     \n     \n    "