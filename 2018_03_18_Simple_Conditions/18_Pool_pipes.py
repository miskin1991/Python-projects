v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

litres_p1 = p1 * h
litres_p2 = p2 * h

litres_both = litres_p1 + litres_p2

if litres_both <= v:
    print("The pool is {0}% full. Pipe 1: {1}%. Pipe 2: {2}%."
          .format(int((litres_both/v) * 100), int((litres_p1 * 100)/litres_both), int((litres_p2 * 100)/litres_both)))
else:
    print("For {0} hours the pool overflows with {1} liters.".format(h, (litres_both-v)))
