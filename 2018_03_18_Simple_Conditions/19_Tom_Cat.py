free_days = int(input())

work_days = 365 - free_days

play_time = work_days * 63 + free_days * 127

if play_time <= 30000:
    print('Tom sleeps well')
    remaining_minutes = 30000 - play_time
    remaining_hours = int(remaining_minutes / 60)
    remaining_minutes = int(remaining_minutes - remaining_hours * 60)
    print('{0} hours and {1} minutes less for play'.format(remaining_hours, remaining_minutes))
else:
    print('Tom will run away')
    extra_minutes = play_time - 30000
    extra_hours = int(extra_minutes / 60)
    extra_minutes = int(extra_minutes - extra_hours * 60)
    print('{0} hours and {1} minutes more for play'.format(extra_hours, extra_minutes))
