import math

w = float(input()) * 100
h = float(input()) * 100

widthWorkspace = 120
heightWorkspace = 70

rows = math.floor(w / widthWorkspace)
cols = math.floor((h - 100) / heightWorkspace)

# print(rows,cols)

seats = rows * cols - 3

print(seats)
