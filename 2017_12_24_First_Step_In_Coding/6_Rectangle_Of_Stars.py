n = 0

while n < 2 or n > 100:
    n = int(input())

print('*'*n)

for i in range(1, n-2):
    line = '*'
    line = line + (' ' * (n-2))
    line = line + '*'
    print(line)

print('*'*n)
