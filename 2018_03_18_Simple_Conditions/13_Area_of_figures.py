import math
figure = input()
figure = figure.lower()


if figure == "circle":
    r = float(input())
    area = math.pi * r * r
elif figure == "rectangle":
    a = float(input())
    b = float(input())
    area = a * b
elif figure == "square":
    a = float(input())
    area = a * a
elif figure == "triangle":
    a = float(input())
    h = float(input())
    area = a * h / 2
else:
    area = 0

print("{0:.3f}".format(area))



