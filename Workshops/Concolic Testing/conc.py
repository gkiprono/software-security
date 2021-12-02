from z3 import *

x=Int('x')
y=Int('y')

#solve(x>2,y<10,x+2*y==7)
s = Solver()
print(s)

s.add(x > 10, y == x + 2)
print(s)
print("Solving constraints in the solver s ...")
print(s.check())

#####################################3

x = Int('x')
y = Int('y')

print(simplify(x+y+2*x+3))
print(simplify(x<y+x+2))
print(simplify(And(x+1>=3,x**2+x**2+y**2+2>=5)))

###################################@4

x, y, z = Reals('x y z')
s = Solver()
s.add(x > 1, y > 1, x + y > 3, z - x < 10)
print(s.check())

m = s.model()
print("x = %s" % m[x])

print("traversing model...")
for d in m.decls():
    print("%s = %s" % (d.name(), m[d]))