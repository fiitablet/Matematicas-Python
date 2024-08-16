from sympy import limit, oo, Symbol

x = Symbol('x') # declaramos la variable simbólica
#y = (x**2 + x + 1) // (x**2 - 1) #poner parentesis ojo y * en medio de las x
y=(x**2-x-6)/(x**2-2)
limit(y, x, 3) # Límite puntual
limit(y, x, oo) # Límite en el infinito
limit(y, x, -oo) # Límite en el menos infinito


limit(y, x, 2**0.5, '-') # Límite por izquierda. ojo como escribo raiz o exp sin cos
limit(y, x, 2**0.5, '+') # Límite por derecha.

import sympy as sp
y = sp.sin(1/x)
limit(y, x, 0) # No existe límite
