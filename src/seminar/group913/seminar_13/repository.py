class Repository:
    def __init__(self, filename="sentinces.txt"):
        self.__filename = filename
        self.__sentinces = []
        self.__load_sentinces()
        
    def __load_sentinces(self):
        with open(self.__filename) as f:
            lines = f.readlines()
        self.__sentinces = [line.strip() for line in lines]
        
    def get_sentinces(self):
        return self.__sentinces 
    
    def add_sentince(self, sentince):
        if sentince in self.__sentinces:
            raise ValueError("Sentince already exists")
            return
        self.__sentinces.append(sentince)
        self.__save_sentinces()
    
    def __save_sentinces(self):
        with open(self.__filename, 'w') as f:
            for sentince in self.__sentinces:
                f.write(sentince + '\n')
                
    def __len__(self):
        return len(self.__sentinces)
    