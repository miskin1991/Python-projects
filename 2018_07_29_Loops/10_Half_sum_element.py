import math

n = int(input())

sum_numbers = 0
number = 0
max_number = -100000000000000
for i in range(0, n):
    number = int(input())
    sum_numbers += number
    if max_number < number:
        max_number = number

sum_numbers -= max_number
if sum_numbers == max_number:
    print('Yes Sum = {0}'.format(sum_numbers))
else:
    diff = int(math.fabs(sum_numbers - max_number))
    print('No Diff = {0}'.format(diff))
