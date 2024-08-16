'''
Defino la función Euler() que dado el valor de un paso h
me aproxima la solución en el intervalo [0 1]
de la ecuación deferencial y' = y + x, y(0) = 1 
cuya solución exacta es...
''' 

import sympy as sp 
x = sp.Symbol('x') 
y = sp.Function('y') 
sp.dsolve(y(x).diff(x) - y(x) - x, ics = {y(0): 1}) #condi inicial ics 


from matplotlib import pyplot as plt 
import numpy as np 

def Euler(h): 
    a = 0 # límite inferior del intervalo 
    b = 1 # límite superior 
    x = [0] # (condicion inicial)
    y = [1] # (condicion inicial)
    for n in range(int((b - a) / h)): 
        x.append(x[n] + h) #agrega un elemento a la lista x 
        y.append(y[n] + h * (y[n] + x[n])) # idem a la lista y 
    def f(x): return -x + 2 * np.exp(x) - 1 # función de la solución exacta 
    x_fun = np.linspace(0, 1, 100, endpoint = 1) 
    plt.plot(x, y) # ploteamos la aproximación. 
    plt.plot(x_fun, [f(i) for i in x_fun], color = "magenta") # Aquí ploteamos la solución exacta. 
    plt.show() 

Euler(0.2) 




