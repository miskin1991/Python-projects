budget = float(input())
period = input()

if period.lower() == 'summer':
    if budget <= 100:
        print('Somewhere in Bulgaria')
        print('Camp - {0:0.2f}'.format(budget * 0.3))
    elif budget <= 1000:
        print('Somewhere in Balkans')
        print('Camp - {0:0.2f}'.format(budget * 0.4))
    else:
        print('Somewhere in Europe')
        print('Hotel - {0:0.2f}'.format(budget * 0.9))
elif period.lower() == 'winter':
    if budget <= 100:
        print('Somewhere in Bulgaria')
        print('Hotel - {0:0.2f}'.format(budget * 0.7))
    elif budget <= 1000:
        print('Somewhere in Balkans')
        print('Hotel - {0:0.2f}'.format(budget * 0.8))
    else:
        print('Somewhere in Europe')
        print('Hotel - {0:0.2f}'.format(budget * 0.9))
else:
    print('Wrong period')
