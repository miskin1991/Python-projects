def print_numbers(start=0, stop=10, step=1):
    stop += 1
    for i in range(start, stop, step):
        print('i = {0}'.format(i))


print_numbers(1, 100, 1)
