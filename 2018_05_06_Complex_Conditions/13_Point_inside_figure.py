h = int(input())
x = int(input())
y = int(input())

vertical_border = False
vertical_inside = False
horizontal_border = False
horizontal_inside = False

if ( h <= x <= 2*h) and (0 <= y <= 4*h):
    #inside vertical rectangle
    if x == h or x == 2*h or y == 0 or y == 4*h:
        vertical_border = True
    else:
        vertical_inside = True

if (0 <= x <= 3 * h) and (0 <= y <= h):
    # inside horizontal rectangle.
    if x == 0 or x == 3 * h or y == 0 or y == h:
        horizontal_border = True
    else:
        horizontal_inside = True

if (horizontal_border == True and vertical_inside == False) or (vertical_border == True and horizontal_inside == False):
    print('border')
elif horizontal_inside or vertical_inside:
    print('inside')
else:
    print('outside')
