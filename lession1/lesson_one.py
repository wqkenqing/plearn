#!/bin/pyhon

class Student(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s: %s' % (self.name, self.score))




if __name__ == '__main__':
    student=Student("ken",99)
    student.print_score()