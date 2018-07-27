VIP_PRICE = 499.99
REGULAR_PRICE = 249.99

budget = float(input())
category = input().lower()
group = int(input())

if group < 5:
    transport = budget * 0.75
elif group < 10:
    transport = budget * 0.60
elif group < 25:
    transport = budget * 0.50
elif group < 50:
    transport = budget * 0.40
else:
    transport = budget * 0.25

budget -= transport

if category == "vip":
    tickets = group * VIP_PRICE
else:
    tickets = group * REGULAR_PRICE

remaining_budget = budget - tickets

if remaining_budget > 0:
    print("Yes! You have {0:0.2f} leva left.".format(remaining_budget))
else:
    print("Not enough money! You need {0:0.2f} leva.".format((remaining_budget * (-1))))
