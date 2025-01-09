from domain import Sentence
from repository import Repository

class Service:
    def __init__(self, repo:Repository):
        self.__repo=repo

    def add(self, sentence_from_ui:str):
        sentence=Sentence(sentence_from_ui)
        self.__repo.add(sentence)

    def get_all(self):
        return self.__repo.get_all()
