type = input()
r = int(input())
c = int(input())

if type == 'Premiere':
    price = 12
elif type == 'Normal':
    price = 7.50
elif type == 'Discount':
    price = 5

try:
    print("{0:.2f}".format(price*r*c))
except NameError:
    print('Error')
