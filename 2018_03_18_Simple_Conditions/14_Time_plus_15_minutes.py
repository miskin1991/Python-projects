hoursIn = int(input())
minutesIn = int(input())

minutes = minutesIn + 15

if minutes >= 60:
    minutes = minutes - 60
    hours = hoursIn + 1
else:
    hours = hoursIn

if hours >= 24:
    hours = hours - 24

print("{0}:{1}{2}".format(hours, int(minutes/10), int(minutes%10)))
