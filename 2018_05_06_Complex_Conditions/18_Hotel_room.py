month = input().lower()
nights = int(input())

if month == 'may' or month == 'october':
    price_studio = 50.00
    price_apartment = 65.00
    if nights > 14:
        price_studio = price_studio * 0.70
        price_apartment = price_apartment * 0.90
    elif nights > 7:
        price_studio = price_studio * 0.95
    total_studio = nights * price_studio
    total_apartment = nights * price_apartment
elif month == 'june' or month == 'september':
    price_studio = 75.20
    price_apartment = 68.70
    if nights > 14:
        price_studio = price_studio * 0.80
        price_apartment = price_apartment * 0.90
    total_studio = nights * price_studio
    total_apartment = nights * price_apartment
else:
    price_studio = 76.00
    price_apartment = 77.00
    if nights > 14:
        price_apartment = price_apartment * 0.90
    total_studio = nights * price_studio
    total_apartment = nights * price_apartment

print('Apartment: {0:0.2f} lv.'.format(total_apartment))
print('Studio: {0:0.2f} lv.'.format(total_studio))
