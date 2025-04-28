def lineDDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1
    steps = 0
    x = x1
    y = y1


    if abs(dx) > abs(dy):
        steps = abs(dx)
    else:
        steps = abs(dy)

    xIncrement = dx / float(steps)
    yIncrement = dy / float(steps)

    setPixel(x, y)
    for k in range(steps):
        x += xIncrement
        y += yIncrement
        setPixel(x, y)

def setPixel(x, y):
    print(f"Plotting points ({x:.1f}, {y:.1f})")

print("Enter x and y for 1st point")
x1 = int(input("X coordinate of 1st point: "))
y1 = int(input("Y coordinate of 1st point: "))

print("Enter x and y for 2nd point")
x2 = int(input("X coordinate of 2nd point: "))
y2 = int(input("Y coordinate of 2nd point: "))

lineDDA(x1, y1, x2, y2)

  
