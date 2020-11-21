from math import sqrt
import sys
class Triangle:
    def __init__(self, coordinate):
        def length(x0, y0, x, y):
            return sqrt((x0 - x) * (x0 - x) + (y0 - y) * (y0 - y))

        self.x1 = coordinate[0]
        self.y1 = coordinate[1]
        self.x2 = coordinate[2]
        self.y2 = coordinate[3]
        self.x3 = coordinate[4]
        self.y3 = coordinate[5]
        self.side1 = length(self.x1, self.y1, self.x2, self.y2)
        self.side2 = length(self.x1, self.y1, self.x3, self.y3)
        self.side3 = length(self.x3, self.y3, self.x2, self.y2)


    def S(self):
        p = self.poluperimetr()
        return sqrt(p * (p - self.side1) * (p - self.side2) * (p - self.side3))


    def poluperimetr(self):
        return (self.side1 + self.side2 +self.side3) / 2


class FileUtilis:
    def __init__(self,filename):
        self.filename = filename
    def __str__(self):
        return


def get_list(filename):
    with open(filename) as i:
        result = list(map(lambda x: x.strip('\n').split(), i.readlines()))
        l = len(result)
        for j in range(l):
            result[j] = list(map(int, result[j]))
    return result
def check(coordinate):
    if len(coordinate) != 6:
        return False
    for i in range(len(coordinate)):
        if str(coordinate[i]).isdigit == False:
            return False
    return True



def main(filename):
    coordinate = get_list(filename)
    arr = []
    for i in range(len(coordinate)):
        if check(coordinate[i]):
            area = Triangle(coordinate[i])
            area1 = area.S()
            arr.append(area1)
            print(area1)
        else:
            print('Координаты треугольника {} не зачтены, потому что неправильный ввод'.format(i))
            arr.append(-1)
    return coordinate[arr.index(max(arr))]
if __name__ == "__main__":
    params = sys.argv
    print(main('C:/Users/liza_/PycharmProjects/python_au/triangle/src.txt'))