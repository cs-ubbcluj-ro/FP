from texttable import Texttable
from random import choice
from services import Service

class Console:
    def __init__(self, service:Service):
        self.__service=service

    @staticmethod
    def __ui_menu():
        table=Texttable()
        header=["Option","Functionality"]
        table.add_row(header)
        table.add_row(["1","Add sentence"])
        table.add_row(["2","Start the game"])
        table.add_row(["5","Exit"])
        print(table.draw())

    def __ui_add(self):
        try:
            sentence=input("sentence=")
            sentence=sentence.strip()
            parts=sentence.split(' ')
            for part in parts:
                if len(part)<3:
                    raise ValueError("Each word must be of at least 3 letters!")
            existing_sentences=self.__service.get_all()
            for each_sentence in existing_sentences:
                if each_sentence.sentence.strip()==sentence:
                    raise ValueError("The sentence already exists!")

            self.__service.add(sentence)

        except ValueError as ve:
            print(ve)

    @staticmethod
    def __show_sentence(sentence, guessed_chars, hangman=""):
        cont=0
        string_to_show=""
        for i in range(len(sentence)):
            if sentence[i] in guessed_chars:
                string_to_show+=sentence[i]
            elif sentence[i]==' ':
                string_to_show+=' '
            elif sentence[i] not in guessed_chars:
                string_to_show+='_'
                cont+=1
        print(string_to_show+"  - "+"'"+hangman+"'")
        if cont==0:
            raise ValueError("You won the game!")

    def __ui_start_the_game(self):
        all_sentences=self.__service.get_all()
        using_sentence=choice(all_sentences)
        words=using_sentence.sentence.split(' ')
        guessed_chars=[]
        for word in words:
            first_letter=word[0]
            last_letter=word[len(word)-1]
            if first_letter not in guessed_chars:
                guessed_chars.append(first_letter)
            if last_letter not in guessed_chars:
                guessed_chars.append(last_letter)
        self.__show_sentence(using_sentence.sentence,guessed_chars)
        self.__ui_play_the_game(using_sentence.sentence,guessed_chars)

    def __ui_play_the_game(self, using_sentence, guessed_chars):
        hangman=""
        final_word="hangman"
        i=0
        while True:
            player_guess=input("guess=")
            if player_guess not in using_sentence or (player_guess in guessed_chars):
                hangman=final_word[0:i+1]
                i+=1
            elif player_guess not in guessed_chars:
                guessed_chars.append(player_guess)
            print(f"User guess: {player_guess}",end="  ")
            try:
                self.__show_sentence(using_sentence,guessed_chars,hangman)
            except ValueError as ve:
                print(ve)
                break
            if hangman=="hangman":
                print("You lost!")
                break




    def run(self):
        while True:
            self.__ui_menu()
            command=input("option=")
            if command=="1":
                self.__ui_add()
            elif command=="2":
                self.__ui_start_the_game()
            elif command=="5":
                print("The program ended!")
                break

