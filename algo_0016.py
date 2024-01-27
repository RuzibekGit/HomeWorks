from math import e

def f(x: float, y: float):
    return (x + y) / (y * y + abs((y*y+2)/(x+x**3/5))) + (e **(y+2))

x, y = input().split()

print(round(f(float(x), float(y)), 2))   