from z3 import *

s = Solver()

x=Int('x')
y=Int('y')

a=Int('a')
b=Int('b')

"""
s.add(2*y==x, x-y>10)

print(s.check())

m = s.model()
print("x=%s" %m[x])

for d in m.decls():
    print("%s = %s" % (d.name(), m[d]))


print()"""

###############################
solve(x==3*y, y-x>-50)
solve(2*b==a)