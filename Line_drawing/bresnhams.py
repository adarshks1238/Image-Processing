def LineBres(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    p = 2 * dy - dx
    x = 0
    y = 0
    Xend = 0

   
    if x1 > x2:
        x = x2
        y = y2
        Xend = x1
    else:
        x = x1
        y = y1
        Xend = x2

    setPoint(x, y)

    while x < Xend:
        x += 1
        if p < 0:
            p = p + 2 * dy
        else:
            y += 1
            p = p + 2 * (dy - dx)
        setPoint(x, y)

def setPoint(x, y):
    print(f"Plotting points ({x}, {y})")

print("Enter x and y for 1st point")
x1 = int(input("X coordinate of 1st point: "))
y1 = int(input("Y coordinate of 1st point: "))

print("Enter x and y for 2nd point")
x2 = int(input("X coordinate of 2nd point: "))
y2 = int(input("Y coordinate of 2nd point: "))

LineBres(x1, y1, x2, y2)