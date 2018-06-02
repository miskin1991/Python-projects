hours_exam = int(input())
minutes_exam = int(input())
hours_arrival = int(input())
minutes_arrival = int(input())

time_exam = (hours_exam * 60) + minutes_exam
time_arrival = (hours_arrival * 60) + minutes_arrival

time_difference = time_exam - time_arrival

make_positive = False
if time_difference < 0:
    print('Late')
    make_positive = True
elif time_difference <= 30:
    print('On time')
else:
    print('Early')

if time_difference != 0:
    if make_positive:
        time_difference *= -1
    hours_difference = time_difference // 60
    minutes_difference = time_difference % 60

    if hours_difference != 0:
        print('{0}'.format(hours_difference), end=':')
        print('{0}{1} hours'.format(minutes_difference // 10, minutes_difference % 10), end=' ')
    else:
        print('{0} minutes'.format(minutes_difference), end=' ')

    if make_positive:
        print('after the start')
    else:
        print('before the start')
