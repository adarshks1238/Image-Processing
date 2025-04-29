import matplotlib.pyplot as plot

def plot_circle(xc, yc, x, y):
    for px, py in [
        (x + xc, y + yc), (-x + xc, y + yc),
        (x + xc, -y + yc), (-x + xc, -y + yc),
        (y + xc, x + yc), (-y + xc, x + yc),
        (y + xc, -x + yc), (-y + xc, -x + yc)
    ]:
        plot.plot(px, py, 'ro')

def midpoint_circle(r, xc, yc):
    x, y = 0, r
    p = 1 - r 
    while x <= y:
        plot_circle(xc, yc, x, y)
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * x+1 - 2 * y
    plot.gca().set_aspect('equal')
    plot.grid(True)
    plot.title("Midpoint Circle Algorithm")
    plot.show()

r = int(input("Radius: "))
x = int(input("X coordinate: "))
y = int(input("Y coordinate: "))
midpoint_circle(r, x, y)
