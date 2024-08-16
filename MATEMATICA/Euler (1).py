'''
Defino la función Euler() que dado el valor de un paso h
me aproxima la solución en el intervalo [0 1]
de la ecuación deferencial y' = y + x, y(0) = 1 
cuya solución exacta es
''' 
import sympy as sp 
x = sp.Symbol('x') 
y = sp.Function('y') 
sp.dsolve(y(x).diff(x) - y(x) - x, ics = {y(0): 1}) 


from matplotlib import pyplot as plt 
import numpy as np 

def Euler(h): 
    a = 0 # límite inferior del intervalo 
    b = 1 # límite superior 
    x = [0] # Cond inicial como un elemento de lista 
    y = [1] # CI 
    for n in range(int((b - a) / h)): 
        x.append(x[n] + h) # append agrega un elemento a la lista x 
        y.append(y[n] + h * (y[n] + x[n])) # idem a la lista y 
    def f(x): return -x + 2 * np.exp(x) - 1 # función de la solución exacta 
    x_fun = np.linspace(0, 1, 100, endpoint = 1) 
    plt.plot(x, y) # ploteamos la aproximación. 
    plt.plot(x_fun, [f(i) for i in x_fun], color = "magenta") # es otra forma de hacer el bucle. Aquí ploteamos la solución exacta. 
    plt.show() 
#esto a parte
Euler(0.2) #mas mini el valor se pega mas
#ej 14
import sympy as sp 
x = sp.Symbol('x') 
y = sp.Function('y') 
sp.dsolve(y(x).diff(x) -1+x-4*y(x), ics = {y(0): 1}) #ojo las condic
from matplotlib import pyplot as plt 
import numpy as np 


def Euler(h): 
    a = 0 # límite inferior del intervalo 
    b = 2 # límite superior 
    x = [0] # Cond inicial como un elemento de lista 
    y = [1] # CI 
    for n in range(int((b - a) / h)): 
        x.append(x[n] + h) # append agrega un elemento a la lista x 
        y.append(y[n] + h * (1 - x[n]+4*y[n])) # original evaluo 
    def f(x): return x/4 + 19*np.exp(4*x)/16 - 3/16 # función de la solución exacta 
    x_fun = np.linspace(0, 2, 100, endpoint = 2) #ojo cond 0 2 y hasta 2 en final
    plt.plot(x, y) # ploteamos la aproximación. 
    plt.plot(x_fun, [f(i) for i in x_fun], color = "magenta")  
    plt.show() 
    
#esto a parte
Euler(0.1)
Euler(0.05)
Euler(0.01)
Euler(0.001)


