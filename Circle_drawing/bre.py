import matplotlib.pyplot as plt

def plot_points(xc, yc, x, y):
    for px, py in [
        (x + xc, y + yc), (-x + xc, y + yc),
        (x + xc, -y + yc), (-x + xc, -y + yc),
        (y + xc, x + yc), (-y + xc, x + yc),
        (y + xc, -x + yc), (-y + xc, -x + yc)
    ]:
        plt.plot(px, py, 'ro')

def bresenham_circle(r, xc, yc):
    x, y, p = 0, r, 3 - 2 * r
    while x <= y:
        plot_points(xc, yc, x, y)
        x += 1
        if p < 0:
            p += 4 * x + 6
        else:
            y -= 1
            p += 4 * (x - y) + 10
    plt.gca().set_aspect('equal')
    plt.grid(True)
    plt.title("Bresenham's Circle")
    plt.show()

r = int(input("Radius: "))
x = int(input("X center: "))
y = int(input("Y center: "))
bresenham_circle(r, x, y)
