import matplotlib.pyplot as plt

def midpointCircle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r
    points = []

    def plotCirclePoints(xc, yc, x, y):
        points.extend([
            (xc + x, yc + y),
            (xc - x, yc + y),
            (xc + x, yc - y),
            (xc - x, yc - y),
            (xc + y, yc + x),
            (xc - y, yc + x),
            (xc + y, yc - x),
            (xc - y, yc - x)
        ])

    plotCirclePoints(xc, yc, x, y)

    while x < y:
        x += 1
        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * (x - y) + 1
        plotCirclePoints(xc, yc, x, y)

    return points


print("Enter center coordinates")
xc = int(input("X center: "))
yc = int(input("Y center: "))
r = int(input("Radius: "))


circle_points = midpointCircle(xc, yc, r)


x_coords, y_coords = zip(*circle_points)
plt.figure(figsize=(6,6))
plt.scatter(x_coords, y_coords, color='green', s=10)
plt.gca().set_aspect('equal')
plt.title('Midpoint Circle Drawing')
plt.grid(True)
plt.show()
