def main():
    product = input().lower()
    city = input().lower()
    quantity = float(input())

    if city == 'sofia':
        price = shop_sofia(product, quantity)
    elif city == 'plovdiv':
        price = shop_plovdiv(product, quantity)
    else:
        price = shop_varna(product, quantity)
    print("{0:0.2f}".format(price))


def shop_sofia(product='coffee', quantity=0):
    if product == 'coffee':
        price = quantity * 0.50
    elif product == 'water':
        price = quantity * 0.80
    elif product == 'beer':
        price = quantity * 1.20
    elif product == 'sweets':
        price = quantity * 1.45
    elif product == 'peanuts':
        price = quantity * 1.60
    return price


def shop_plovdiv(product='coffee', quantity=0):
    if product == 'coffee':
        price = quantity * 0.4
    elif product == 'water':
        price = quantity * 0.7
    elif product == 'beer':
        price = quantity * 1.15
    elif product == 'sweets':
        price = quantity * 1.30
    elif product == 'peanuts':
        price = quantity * 1.50
    return price


def shop_varna(product='coffee', quantity=0):
    if product == 'coffee':
        price = quantity * 0.45
    elif product == 'water':
        price = quantity * 0.70
    elif product == 'beer':
        price = quantity * 1.10
    elif product == 'sweets':
        price = quantity * 1.35
    elif product == 'peanuts':
        price = quantity * 1.55
    return price


main()
