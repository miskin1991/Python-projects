v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

litres_p1 = p1 * h
litres_p2 = p2 * h

if (litres_p1 + litres_p2) <= v:
    total = int(((litres_p1 + litres_p2)/v) * 100)
    pipe1 = int((litres_p1/(litres_p1+litres_p2))*100)
    pipe2 = int((litres_p2/(litres_p1+litres_p2))*100)
    print("The pool is {0}% full. Pipe 1: {1}%. Pipe 2: {2}%.".format(total, pipe1, pipe2))
else:
    print("For {0} hours the pool overflows with {1} liters.".format(h, ((litres_p1+litres_p2)-v)))

