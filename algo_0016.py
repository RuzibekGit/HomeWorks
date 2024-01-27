
def f(x: float, y: float):
    return (x + y) / ((y**2 + (y**2+2)/(x+y**(3/5)))**0.5) + (2.71828**(y+2))

x, y = input().split()

print(round(f(float(x), float(y)), 2))   