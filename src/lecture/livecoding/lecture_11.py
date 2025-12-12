"""
    Lecture 11 - the Services layer, Design Patterns

    What are Design Patterns?
        - people figured out that many problems in writing software keep repeating over
        and over
        - design patterns are template (generic) solutions that when implemented, can
        help
        - a common way to solve common problems

    What Design Patterns have we already come across?
        Iterator
            - solves the problem of traversing a collection, so that we visit each
            element exactly once
            - look up implementation of MemoryRepository in Bakery example
            learn more at https://refactoring.guru/design-patterns/iterator

        Layered Architecture
            - very high-level pattern, which provides a suitable (not perfect, not unique)
            way of organizing a large program
            - programs are organized into layers ( ui -> services -> repository)
            - each layer talks within itself or with the layer immediately below
            - look up week 10 lecture notes in the source code (bakery example)

        Memento
            - remember the state of an object and revert to it when needed
            - we use it when copying the list of entities for undo/redo (it's not
            an exact implementation of the pattern though :( )
            -- learn more - https://refactoring.guru/design-patterns/memento

        Command
            - Remember an operation (and its parameters) and carry it out sometime later
            - Used for undo/redo in many cases
            - Learn more at -- https://refactoring.guru/design-patterns/command
"""

"""
    In Python, function are "first class citizens" => they can be used like any variable (assigned, function parameters etc)
"""


def f(a, b, c):
    print(a, b, c)


# this implements the Command part of the command design pattern
class FunctionCall:
    def __init__(self, function, *params):
        self._function = function
        self._params = params

    def call(self):
        self._function(*self._params)  # * to unpack the parameters

    def __call__(self, *args, **kwargs):
        self.call()


"""
    The program's undo/redo stack consists of Operation objects
"""


class Operation:
    def __init__(self, undo_function: FunctionCall, redo_function: FunctionCall):
        self.__undo = undo_function
        self.__redo = redo_function

    def undo(self):
        self.__undo.call()

    def redo(self):
        self.__redo.call()


undo_function = FunctionCall(f, 1, 2, 3)
undo_function.call()
undo_function()

# 5()
