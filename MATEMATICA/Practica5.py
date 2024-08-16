
import sympy as sp 

# 2.b) 
k = sp.Symbol('k') # definimos una constante como variable simbólica 
x = sp.Symbol('x') # definimos la variable de integración como simbólica 
y = sp.Function('y') # y es la función, por eso se define de esta manera. 
y0 = sp.Symbol('y0') # La otra constante que proponemos de manera genérica como condición inicial. 

f1 = k * y(x) # Expreso la ecuación aquí, pero podría hacerlo directamente dentro del dsolve, como en el ejercicio 2.d. 
ics = {y(0): y0} # Se introduce la condición inicial como un diccionario. 
soluc = sp.dsolve(y(x).diff(x) - f1, ics = ics) # Ponemos el "- f1" porque es como igualar la eq diferencial a cero. 
soluc

''' 
Una notación que usa el módulo sympy de Python para la primera derivada es: y(x).diff(x), que es equivalente al dy/dx.  Para la segunda: y(x).diff(x,x) y así sucesivamente para las de orden mayor. La condición inicial (opcional) se introduce como ics={y(x0)=y0} (la llave es por ser un diccionario de Python). 

La salida de sp.Eq(), o como lo expresa la consola Eq, es una ecuación, cuyo primer argumento es el lado izquierdo de la igualdad y su segundo argumento, el lado derecho. 
''' 

# Si deseamos asignar valores a variables o parámetros en las expresiones, lo haremos con el método subs() 

soluc.subs(y0, 8) # sub() reemplaza las coincidencias por lo que le especifiquemos. 

# 2.d) 
sp.dsolve((1 + x) * y(x).diff(x) - y(x)) 


# Graficar curvas solución: 
    # Si queremos graficar una solución, podemos usar las librerías conocidas. Por ejemplo, usando mpmath: 

import mpmath 
import sympy as sp 

x = sp.Symbol('x') 
y = sp.Function('y') 

ics = {y(-1): -1} 
sol = sp.dsolve(x**2 * y(x).diff(x) - y(x) + x * y(x), ics = ics) 

sol = lambda x: mpmath.exp(-1) * mpmath.exp(-1/x)/x # entramos la solución como función anónima 
mpmath.plot(sol, [-6, 10], [-2, 1]) 




# Campo de direcciones: 
''' Aquí hay que probar los límites, la distancia entre vectores, etc. La idea es que consigamos un
 gráfico ilustrativo del comportamiento de la ecuación. 

Los 4 parámetros de quiver: 
t: Representa la posición horizontal 
y: Representa la posición vertical 
1/n: Representa la longitud de las flechas, donde n es la norma del vector de velocidad calculado en 
cada punto.
u/n: Representa la dirección de las flechas, donde u es la componente horizontal del vector de
 velocidad y n es la norma del vector de velocidad. 

Probemos con la ecuación y' = y(3-y) 
''' 

import matplotlib.pyplot as plt
import numpy as np
#-10min  10max 1 el paso/dist
t, y = np.meshgrid(np.arange(-10, 10, 1), np.arange(-2, 5, 0.5)) #creo una grilla bidireccional que se modifica
u = y * (3 - y) # siempre despejar y' u es yprima 
n = np.sqrt(u**2 + 1**2) # Normalizamos el vector 
plt.quiver(t, y, 1/n, u/n) # ver arriba 
plt.xlim(-10, 10)
plt.ylim(-2, 5)
plt.show() 


''' También podríamos desear graficar la trayectoria de una solución sobre el campo de direcciones. Usando solve_ivp podemos hacerlo muy fácilmente. 

Los 4 parámetros que le daremos como input a solve_ivp son 
solve_ivp(fun, t_span, y0, t_eval) 

fun representa la función que define la EDO 
t_span define el intervalo de tiempo sobre el que se quiere resolver la EDO. 
y0 especifica la condición inicial 
t_eval determina los puntos de evaluación en los que se desea calcular la solución. En este caso, se evalúa la solución en 1000 puntos distribuidos uniformemente entre t = 0 y t = 10, con un paso de 0.01 entre cada punto. 

Supongamos que y(0) = 2''' 

from scipy.integrate import solve_ivp

t, y = np.meshgrid(np.arange(-1, 10, 0.5), np.arange(-2, 5, 0.5)) 
u = y * (3 - y) 
n = np.sqrt(u**2 + 1**2) 
plt.quiver(t, y, 1/n, u/n) 

F = lambda t, y: y * (3 - y) 
t_eval = np.arange(0, 10, 0.01)
sol = solve_ivp(F, [0, 10], [2], t_eval = t_eval) # ver arriba 
plt.plot(sol.t, sol.y[0]) 

plt.xlim(-1, 10)
plt.ylim(-2, 5)
plt.show() 
sol.y

# vean qué contiene sol.t y sol.y 

''' En ciertos contextos puede ser muy ilustrativo superponer varias trayectorias en el mismo gráfico, cambiando la condición inicial. Con un bucle for, lo podemos hacer de manera muy elegantge ''' 

t, y = np.meshgrid(np.arange(-1, 4, 0.2), np.arange(-2, 6, 0.5)) 
u = y * (3 - y) 
n = np.sqrt(u**2 + 1**2) 
plt.quiver(t, y, 1/n, u/n) 

F = lambda t, y: y * (3 - y) 
t_eval = np.arange(0, 10, 0.01)
for c in np.arange(-1, 4, 0.5): # ¿Qué hace esto? 
    sol = solve_ivp(F, [0, 10], [c], t_eval = t_eval) 
    plt.plot(sol.t, sol.y[0]) 

plt.xlim(-1, 4)
plt.ylim(-2, 6)
plt.show() 



