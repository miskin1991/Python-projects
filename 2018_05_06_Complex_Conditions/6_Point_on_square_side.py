class Point:
    x = 0.0
    y = 0.0

    def __init__(self, px=0, py=0):
        self.x = px
        self.y = py

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class Square:
    x1 = 0.0
    y1 = 0.0
    x2 = 0.0
    y2 = 0.0

    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def get_x1(self):
        return self.x1

    def get_y1(self):
        return self.y1

    def get_x2(self):
        return self.x2

    def get_y2(self):
        return self.y2


def inside_square(point, square):
    if ((point.get_x() == square.get_x1() or point.get_x() == square.get_x2())
            and (square.get_y1() <= point.get_y() <= square.get_y2())):
        print('Border')
    elif ((point.get_y() == square.get_y1() or point.get_y() == square.get_y2())
            and (square.get_x1() < point.get_x() < square.get_x2())):
        print('Border')
    else:
        print('Inside / Outside')


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x = float(input())
y = float(input())

my_sqare = Square(x1, y1, x2, y2)
my_point = Point(x, y)
inside_square(my_point, my_sqare)
