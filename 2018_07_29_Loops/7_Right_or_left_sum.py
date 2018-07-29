import math

n = int(input())

# sum first n numbers
left_sum = 0
for i in range(0, n):
    left_sum += int(input())

# sum second n numbers
right_sum = 0
for i in range(0, n):
    right_sum += int(input())

difference = int(math.fabs(left_sum - right_sum))

if difference == 0:
    print('Yes, sum = {0}'.format(left_sum))
else:
    print('No, diff = {0}'.format(difference))
