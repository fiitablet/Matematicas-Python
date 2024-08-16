import sympy as sp
x = sp.Symbol('x')
y =(x**2-x-6)/(x**2-2)

y =sp.cos(x) #agrego sp. para tan cos sin log e raiz sqrt de(x) o de lo que sea
y=sp.sqrt(x) #raiz
#y=1//2 asi divido comun con 2 palitos ojo
sp.diff(y, x)

sp.diff(y, x, x) # derivada segunda.
sp.diff(y, x, 2) # Otra forma de escribirla.  



#grafico de la fc original
import mpmath
mpmath.plot(lambda x: (x**3)/(x-1))
