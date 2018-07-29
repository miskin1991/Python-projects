import math

n = int(input())

sum_odd = 0
sum_even = 0

for i in range(0, n):
    if i % 2 == 0:
        sum_even += int(input())
    else:
        sum_odd += int(input())

difference = int(math.fabs(sum_odd - sum_even))

if difference == 0:
    print('Yes Sum = {0}'.format(sum_even))
else:
    print('No Diff = {0}'.format(difference))
