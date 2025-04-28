import matplotlib.pyplot as plot

def LineBres(x1, y1, x2, y2):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    p = 2 * dy - dx
    x = x1
    y = y1
    Xend = x2

    
    if x1 > x2:
        x = x2
        y = y2
        Xend = x1

    points = []
    def setPoint(x, y):
        print(f"Plotting points ({x}, {y})")
        points.append((x, y))

    setPoint(x, y)

    while x < Xend:
        x += 1
        if p < 0:
            p = p + 2 * dy
        else:
            y += 1
            p = p + 2 * (dy - dx)
        setPoint(x, y)

    return points


print("Enter x and y for 1st point")
x1 = int(input("X coordinate of 1st point: "))
y1 = int(input("Y coordinate of 1st point: "))

print("Enter x and y for 2nd point")
x2 = int(input("X coordinate of 2nd point: "))
y2 = int(input("Y coordinate of 2nd point: "))


line_points = LineBres(x1, y1, x2, y2)


x_coords, y_coords = zip(*line_points)


plot.figure(figsize=(6,6))
plot.scatter(x_coords, y_coords, color='blue', s=10)
plot.plot(x_coords, y_coords, color='blue', linewidth=1)
plot.gca().set_aspect('equal')
plot.title('Bresenham Line Drawing')
plot.grid(True)
plot.show()
