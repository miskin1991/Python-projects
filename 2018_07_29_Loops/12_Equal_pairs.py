import math

n = int(input())

a = int(input())
b = int(input())

value = a + b
diff = 0
for i in range(2, n):
    a = int(input())
    b = int(input())
    if (math.fabs(a + b - value)) > diff:
        diff = int(math.fabs(a + b - diff))
        value = a + b

if diff > 0:
    print("No, maxdiff={0}".format(diff))
else:
    print("Yes, value={0}".format(value))
