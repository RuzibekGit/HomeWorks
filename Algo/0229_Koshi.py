# res = "="
# a, b = input().split()
# a, b = round((int(a)+int(b))/2, 2), round((int(a)*int(b))**0.5, 2)
# if   a > b: res = ">"
# elif a < b: res = "<"
# print(res)



import math

def f(a, b):
    a, b = (a + b) / 2, math.sqrt(a * b)

    if a > b: return ">"
    if a < b: return "<"
    return "="

a, b = input().split()
print(f(int(a), int(b)))
