n1 = int(input())
n2 = int(input())
operator = input()


def print_primary_operation(a=0, b=0, action='+', res=0):
    if res % 2 == 0:
        print("{0} {1} {2} = {3} - even".format(a, action, b, res))
    else:
        print("{0} {1} {2} = {3} - odd".format(a, action, b, res))


if operator == '+':
    result = n1 + n2
    print_primary_operation(n1, n2, operator, result)
elif operator == '-':
    result = n1 - n2
    print_primary_operation(n1, n2, operator, result)
elif operator == '*':
    result = n1 * n2
    print_primary_operation(n1, n2, operator, result)
elif operator == '/':
    if n2 == 0:
        print("Cannot divide {0} by zero".format(n1))
    else:
        result = n1 / n2
        print("{0} {1} {2} = {3:0.2f}".format(n1, operator, n2, result))
else:
    if n2 == 0:
        print("Cannot divide {0} by zero".format(n1))
    else:
        result = n1 % n2
        print("{0} {1} {2} = {3}".format(n1, operator, n2, result))
