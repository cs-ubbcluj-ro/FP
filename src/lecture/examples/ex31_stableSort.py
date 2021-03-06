from random import choice


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    def __str__(self):
        return str(self.age) + ' ' + self.name


def generate():
    """
    Generate some people instances
    """
    result = []

    famName = ['Popescu', 'Marian', 'Pop', 'Lazarescu', 'Dincu']
    givName = ['Anca', 'Emilia', 'Liviu', 'Marius']
    age = [17, 18, 19, 20]

    for i in range(20):
        result.append(Person(choice(famName) + ' ' + choice(givName), choice(age)))

    return result


'''
1. Generate people
'''
result = generate()

'''
2. First we sort the list by name (ascending)
'''
result.sort(key=lambda p: p.name)

'''
3. Then we sort by age (descending) - the sorts are STABLE
'''
result.sort(key=lambda p: p.age, reverse=True)

'''
4. People of the same age are ordered by name
'''
for p in result:
    print(p)
