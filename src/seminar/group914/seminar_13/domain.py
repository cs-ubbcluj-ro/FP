class Sentence:
    def __init__(self, sentence:str):
        self.__sentence=sentence

    @property
    def sentence(self):
        return self.__sentence

    def __str__(self):
        return f"sentence={self.sentence}"

