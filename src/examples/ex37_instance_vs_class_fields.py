"""
Created on Nov 2, 2016

@author: Arthur
"""


class Student:
    # Class field is shared by all instances
    __studentCount = 0

    def __init__(self, name="Anonymous"):
        self.__name = name

        '''
            NB!
            Make sure to prefix the attribute name with:
                - class name, or
                - type(self)
        '''
        Student.__studentCount += 1

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    @staticmethod
    def get_student_count():
        return Student.__studentCount


if __name__ == "__main__":
    '''
        We create some students
    '''
    s1 = Student()
    s2 = Student()

    s1.set_name("Anna")
    s2.set_name("Carla")

    print(s1.get_name())
    print(s2.get_name())

    print(Student.get_student_count())

    '''
        What happens here?
    '''
    # print(student.__studentCount)
