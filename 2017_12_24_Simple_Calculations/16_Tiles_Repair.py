n = int(input())
w = float(input())
l = float(input())
m = int(input())
o = int(input())

areaPlace = n ** 2
areaBrick = w * l
areaBench = m * o

totalBricks = (areaPlace - areaBench) / areaBrick

amountOfTime = totalBricks * 0.2

print("{0:.2f}".format(totalBricks))
print("{0:.2f}".format(amountOfTime))
