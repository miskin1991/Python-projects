estimate_hours = int(input())
available_days = int(input())
employees = int(input())

work_hours = (available_days * 0.90) * 8
work_hours_extra = employees * (available_days * 2)

total_hours = int(work_hours + work_hours_extra)

if total_hours >= estimate_hours:
    print('Yes!{0} hours left.'.format(total_hours-estimate_hours))
else:
    print('Not enough time!{0} hours needed.'.format(estimate_hours - total_hours))
