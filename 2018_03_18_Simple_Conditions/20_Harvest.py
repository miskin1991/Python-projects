import math
x_area = int(input())
y_grape_kg_line = float(input())
z_target_litres = int(input())
n_employees = int(input())

grape_area = x_area * 0.40
total_grape_kg = grape_area * y_grape_kg_line
total_litres = total_grape_kg / 2.5

if total_litres < z_target_litres:
    print('It will be a tough winter! More {0} liters wine needed.'.format(math.floor(z_target_litres - total_litres)))
else:
    print('Good harvest this year! Total wine: {0} liters.'.format(math.floor(total_litres)))
    litres_above = total_litres - z_target_litres
    print('{0} liters left -> {1} liters per person.'
          .format(math.ceil(litres_above), math.ceil(litres_above / n_employees)))
