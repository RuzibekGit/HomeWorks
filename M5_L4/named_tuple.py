print("hi")

e = (1, 2, 3)

print(*e)
a, b, c = e
print(a,b,c)
n, *m = e
print(n,m)
c = (1,)
print(type(c))

v = range(10)
d, v, *f = v
print(d,v,f)