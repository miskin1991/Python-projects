import math

year = input()
p = int(input())
h = int(input())

games_sofia = (48 - h) * 0.75
games_home_town = h

games_holidays = float(p) * 2 / 3

total_games = games_sofia + games_home_town + games_holidays

if year == 'leap':
    total_games = total_games * 1.15

print(math.floor(total_games))
