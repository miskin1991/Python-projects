a = int(input())
b = int(input())
c = int(input())

totalSeconds = a + b + c

minutes = int(totalSeconds / 60)
seconds = totalSeconds - minutes * 60

print("{0}:{1}{2}".format(minutes, int(seconds/10), seconds%10))
