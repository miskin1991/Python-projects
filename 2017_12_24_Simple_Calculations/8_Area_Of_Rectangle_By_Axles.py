x1 = float(input())
y1 = float(input())

x2 = float(input())
y2 = float(input())

width = abs(x1 - x2)
height = abs(y1 - y2)

area = width * height
perimeter = 2 * (width + height)

print(area)
print(perimeter)
