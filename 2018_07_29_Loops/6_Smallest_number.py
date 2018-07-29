n = int(input())

min_num = int(input())

for i in range(0, n-1):
    current_num = int(input())
    if current_num < min_num:
        min_num = current_num

print(min_num)
