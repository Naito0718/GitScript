import sympy as sym

x= sym.Symbol('x')

y=sym.diff(sym.arctan(x),x)
z=sym.diff(sym.tan(x)/x,x)
print(y)
print(z)