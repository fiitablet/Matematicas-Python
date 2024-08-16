import sympy as sp  
k = sp.Symbol('k') # definimos una constante como variable simbólica 
x = sp.Symbol('x') # definimos la variable de integración como simbólica 
y = sp.Function('y') # y es la función, por eso se define de esta manera. 

f1 = k * y(x) # Expreso la ecuación aquí, pero podría hacerlo directamente dentro del dsolve
sp.dsolve(y(x).diff(x) - f1) # Ponemos el "- f1" porque es como igualar la eq diferencial a cero. 

"""La condición inicial se pone como ics={y(x0)=y0}. ""
La salida de sp.Eq() es una ecuación, cuyo primer argumento es lado izquierdo
 de la igualdad y su segundo argumento, el lado derecho. 
"""

#ej 
f2 = y(x)**2 
ics = {y(1): 4} # Se introduce la condición inicial 
sp.dsolve(y(x).diff(x) - f2, ics = ics) 

# Campo de direcciones: 
import matplotlib.pyplot as plt
import numpy as np

x, y = np.meshgrid(np.arange(0, 10, 0.5),np.arange(-1, 5.5, 0.5))
 # creamos una grilla en "x" y en "y" con paso 0.5 en cada caso. 
u = -y * (y - 2) * (y - 4) / 10 # ecuación diferencial segun caso
n = np.sqrt(u**2 + 1**2)  #Normalizamos el vector 
plt.quiver(x, y, 1/n, u/n) # define las flechas, su longitud   
plt.xlim(0, 10) 
plt.ylim(-1, 5) 
plt.show() 


#graficar trayectorias, podemos usar solve_ivp 
from scipy.integrate import solve_ivp  #metodo mas rapido
import numpy as np 

#todo el bloque hago todo junto ej:
F = lambda x, y: -y * (y - 2) * (y - 4) / 10 
t_eval = np.arange(0, 10, 0.01) # evaluo entre 0 y 10,con paso de 0.01
for i in np.arange(-1, 5, 0.5): # usamos un for para varias trayectoria 
    sol = solve_ivp(F, [0, 10], [i], t_eval = t_eval) 
    plt.plot(sol.t, sol.y[0])  #linea de una sola trayectoria 

x, y = np.meshgrid(np.arange(0, 10, 0.5), np.arange(-1, 5.5, 0.5))
u = -y * (y - 2) * (y - 4) / 10 
n = np.sqrt(u**2 + 1**2) # Normalizamos el vector 
plt.quiver(x, y, 1/n, u/n)
plt.xlim(0, 10)
plt.ylim(-1, 5)
plt.show() 





