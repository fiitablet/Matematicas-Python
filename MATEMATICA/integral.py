import sympy as sp 
x, y = sp.symbols('x y')
#Integrales
sp.integrate(sp.exp(-x), (x, 0, sp.oo)) # integral definida evaluo en 0 y infinito
sp.integrate(1 / x**2) # integral indefinida sin nada es directo
#sp.integrate(sp.cos(2*x)) ej sp para casos raros sin e cos tan sqrt
#sp.integrate(sp.sqrt(x**2))
#sp.integrate(sp.exp(3*x))



