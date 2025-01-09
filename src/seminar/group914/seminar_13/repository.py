from domain import Sentence

class Repository:
    def __init__(self, file_name="sentences.txt"):
        self.__data=[]
        self.__file_name=file_name
        self.__load()

    def add(self, sentence:Sentence):
        self.__data.append(sentence)
        self.__save()

    def __iter__(self):
        return iter(self.__data)

    def get_all(self):
        return self.__data

    def __load(self):
        try:
            fin=open(self.__file_name,"rt")
            lines=fin.readlines()
            for line in lines:
                if line.strip():
                    sentence=line.strip()
                    sentence_to_put=Sentence(sentence)
                    self.__data.append(sentence_to_put)
            fin.close()
        except FileNotFoundError:
            pass

    def __save(self):
        fout=open(self.__file_name,"wt")
        for sentence in self.__data:
            fout.write(sentence.sentence+"\n"+"\n")
        fout.close()
