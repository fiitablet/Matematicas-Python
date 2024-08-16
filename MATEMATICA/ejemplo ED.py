import sympy as sp 
#solucion excata con sp

#declaro var simbolicas
k = sp.Symbol('k') # definimos una constante como variable simbólica 
x = sp.Symbol('x') # definimos la variable de integración como simbólica 
y = sp.Function('y') # y es la función, por eso se define de esta manera. 
c = sp.Symbol('c') # y es la función, por eso se define de esta manera. 

 # Condiciones iniciales: 
ics = {y(2): 5} # Se introduce la condición inicial como un diccionario. 
sp.dsolve(y(x).diff(x)*x+3*y(x)-5*x**2) # ojo poner derivada q era diff la fc ori

sp.dsolve(y(x).diff(x)*x+3*y(x)-5*x**2 , ics = ics)   #da exacto con la fc original otra vez y da con -8 

#quiero ver que pasa con valores de c

from matplotlib import pyplot as plt
import numpy as np

def f(x): return (8*c + x**5 - 32)/(x**3)
x = np.linspace (-10, 10, 201, endpoint=10)
for c in range (3, 8):
    plt.plot (x, [f(i) for i in x]) 
plt.ylim (-20, 20)
plt.show()

# Campo de direcciones: 

import matplotlib.pyplot as plt
import numpy as np

x, y = np.meshgrid(np.arange(0, 10, 0.5),np.arange(-20, 20, 2)) # creamos una grilla de puntos en "x" y en "y" con paso 0.5 en cada caso. 
u =0.1*y-np.sin(y)   # ecuación diferencial 
n = np.sqrt(u**2 + 1**2) # Normalizamos el vector,para solo mostrar mejor
plt.quiver(x, y, 1/n, u/n) # define las flechas, su longitud y otras cosas más  
plt.xlim(0, 10) 
#plt.ylim(-1, 5) 
plt.show() 


# Si quisiera graficar trayectorias, podemos usar solve_ivp que sería equivalente a ODE45 de Matlab (recordar que para varias curvas simultáneamente, hay que marcar todo y correr con F9). solve_ivp usa un método de Runge Kutta: 
from scipy.integrate import solve_ivp  #metodo mas rapido
import numpy as np 

#todo el bloque hago ojo
F = lambda x, y:0.1*y-np.sin(y)
t_eval = np.arange(0, 10, 0.01) #donde evaluo entre 0 y 10,con paso de 0.01
for i in np.arange(-15, 15, 1): # usamos un for para marcar varias trayectorias 
    sol = solve_ivp(F, [0, 10], [i], t_eval = t_eval) 
    plt.plot(sol.t, sol.y[0])  #lineaaa buena dee una sola trayectoria 

x, y = np.meshgrid(np.arange(0, 10, 0.5), np.arange(-20, 20, 2))
u = 0.1*y-np.sin(y)
n = np.sqrt(u**2 + 1**2) # Normalizamos el vector 
plt.quiver(x, y, 1/n, u/n)
plt.xlim(0, 10)
plt.ylim(-20, 20)
plt.show() 



          




