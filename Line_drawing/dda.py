import matplotlib.pyplot as plt

def lineDDA(x1, y1, x2, y2):
    dx = x2 - x1
    dy = y2 - y1

    steps = abs(dx) if abs(dx) > abs(dy) else abs(dy)

    xinc = dx / float(steps)
    yinc = dy / float(steps)

    x = x1
    y = y1

    points = []

    def setPixel(x, y):
        print(f"Plotting points ({x:.1f}, {y:.1f})")
        points.append((round(x), round(y)))

    setPixel(x, y)
    for k in range(int(steps)):
        x += xinc
        y += yinc
        setPixel(x, y)

    return points

print("Enter x and y for 1st point")
x1 = int(input("X coordinate of 1st point: "))
y1 = int(input("Y coordinate of 1st point: "))

print("Enter x and y for 2nd point")
x2 = int(input("X coordinate of 2nd point: "))
y2 = int(input("Y coordinate of 2nd point: "))


line_points = lineDDA(x1, y1, x2, y2)


x_coords, y_coords = zip(*line_points)


plt.figure(figsize=(6,6))
plt.scatter(x_coords, y_coords, color='blue', s=10)
plt.plot(x_coords, y_coords, color='blue', linewidth=1)
plt.gca().set_aspect('equal')
plt.title('DDA Line Drawing')
plt.grid(True)
plt.show()
