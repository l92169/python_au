from math import sqrt
import sys


class Point:
    pass

class Triangle:
    def __init__(self,filename):
        self.filename = filename

    def S(self,perimetr,l1,l2,l3):
        return sqrt(perimetr * (perimetr - l1) * (perimetr - l2) * (perimetr - l3))
    def length(self,x1,y1,x2,y2,x3,y3):
        l1 = sqrt((x2 - x1)^2 + (y2 - y1)^2)
        l2 = sqrt((x3 - x2) ^ 2 + (y3 - y2) ^ 2)
        l3 = sqrt((x3 - x1) ^ 2 + (y3 - y1) ^ 2)


class FileUtilis:
    def __init__(self,filename):
        self.filename = filename


    def get_all_lines(filename):
        file = open(filename)
        result = file.readlines()
        file.close()
        return result


def main(filename):

if __name__ == "__main__":
    main()