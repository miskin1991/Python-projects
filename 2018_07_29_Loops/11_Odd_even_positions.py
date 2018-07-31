n = int(input())

number = 0
odd_sum = 0
odd_min = 100000000000000
odd_max = -100000000000000
even_sum = 0
even_min = 100000000000000
even_max = -100000000000000
for i in range(0, n):
    number = float(input())
    if i % 2 != 0:
        even_sum += number
        if even_max < number:
            even_max = number
        if even_min > number:
            even_min = number
    else:
        odd_sum += number
        if odd_max < number:
            odd_max = number
        if odd_min > number:
            odd_min = number

print("OddSum={0},".format(str(odd_sum if odd_sum % 1 else int(odd_sum))))
if odd_min == 100000000000000:
    print("OddMin=No,")
else:
    print("OddMin={0},".format(str(odd_min if odd_min % 1 else int(odd_min))))
if odd_max == -100000000000000:
    print("OddMax=No,")
else:
    print("OddMax={0},".format(str(odd_max if odd_max % 1 else int(odd_max))))
print("EvenSum={0},".format(str(even_sum if even_sum % 1 else int(even_sum))))
if even_min == 100000000000000:
    print("EvenMin=No,")
else:
    print("EvenMin={0},".format(str(even_min if even_min % 1 else int(even_min))))
if even_max == -100000000000000:
    print("EvenMax=No")
else:
    print("EvenMax={0}".format(str(even_max if even_max % 1 else int(even_max))))
