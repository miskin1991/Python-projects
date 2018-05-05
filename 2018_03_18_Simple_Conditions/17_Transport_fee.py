def by_taxi(kilometers=0, time='day'):
    price = 0.70

    if time == 'day':
        price = price + kilometers * 0.79
    else :
        price = price + kilometers * 0.90

    return price


def by_bus(kilometers=0):
    return kilometers * 0.09


def by_train(kilometers=0):
    return kilometers * 0.06


n = int(input())
time = input()

if n < 20:
    price = by_taxi(n, time)
elif n < 100:
    price = by_bus(n)
else:
    price = by_train(n)

print("{0:0.2f}".format(price))
