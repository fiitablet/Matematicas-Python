
# Gráficos en 3D: 

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-5, 5, 100) # Valores en x en el grafico se modifica -el 100
y = np.linspace(-5, 5, 100) # Valores en y 
X, Y = np.meshgrid(x, y) # Creamos la grilla. Noten que las variables en mayúscula son diferentes que las minúsculas. 
Z = np.sin(np.sqrt(X**2 + Y**2)) # Dados que ya saben usar lo básico de Python, ¿Cuál es esta superficie? 
#todo mayuscula Z X Y OJO 
#Z= X**2-Y**2 

# Crear figura y ejes 3D. Todo esto correrlo junto. 
fig = plt.figure() # Abre una figura vacía. 

ax = fig.add_subplot(111, projection = '3d') # Creamos un subplot en la figura con una disposición de subgráficos de 1 fila y 1 columna, y seleccionamos el primer (y único) subplot en esa disposición. El número 111 es una forma compacta de especificar esta disposición de subgráficos.

surf = ax.plot_surface(X, Y, Z) # Graficar superficie

plt.gca().mouse_init() # Activamos la herramienta de rotación interactiva. 

ax.set_xlabel('Eje X') # Etiqueta eje x 
ax.set_ylabel('Eje Y') # Etiqueta eje y 
ax.set_zlabel('Eje Z') # Etiqueta eje z 

plt.show()



# Curvas de nivel - Usamos la función definida recién. TODO JUNTO

fig, ax = plt.subplots()
cnt = ax.contour(X, Y, Z, levels = 5) # Creamos las curvas de nivel. Seteamos cuántos niveles queremos. 
ax.clabel(cnt, cnt.levels, inline = True, fontsize = 10) # Mostramos directamente en el gráfico cuál es cada nivel de z. 
plt.show()


# Otra manera muy bonita de graficar las curvas de nivel: 
fig, ax = plt.subplots()
cnt = ax.contourf(X, Y, Z) # Es como contour, pero pinta cada nivel. 
cbar = ax.figure.colorbar(cnt, ax = ax) # Agregamos la leyenda al costado. 
cbar.ax.set_ylabel("Nivel del eje z", rotation = -90, va = "bottom")
plt.show() 



# Derivadas parciales 

from sympy import symbols, diff, sin, cos, exp

x, y = symbols('x y')

f = sin(x) * cos(y) + exp(x*y)

ddf_dx = diff(f, x) # Derivada parcial de f con respecto a x

ddf_dy = diff(f, y) # Derivada parcial de f con respecto a y

x0 = 0
y0 = 0

# Evaluamos las derivadas parciales en el punto (x0, y0) usando el método subs que sustituye valores en variables. 
ddf_dx.subs({x: x0, y: y0})
ddf_dy.subs({x: x0, y: y0})



# Derivada direccional y gradiente 
from sympy import symbols, diff, sqrt 
import numpy as np 

# Definir las variables simbólicas
x, y = symbols('x y')

# Definir i y j 
i = np.array([1, 0]) 
j = np.array([0, 1]) 

# Definir la función
f = 3 * x**2 - 2 * y**2 

# Definir el punto en el que se evalúa la derivada direccional
x0 = -3/4 
y0 = 0

# Definir la dirección del vector 
u = np.array([3/4, 1]) 

# Calcular el gradiente de la función evaluado en el punto 
f_x = diff(f, x) 
f_y = diff(f, y) 
f_x = f_x.subs(x, x0) 
f_y = f_y.subs(y, y0) 

gradiente_en_P = f_x * i + f_y * j 

# Calcular la norma de u y normalizarlo 
norm_u = sqrt(u[0]**2 + u[1]**2)
u_normalizado = u / norm_u 

# Calcular la derivada direccional 
np.dot(gradiente_en_P, u_normalizado) 



# Integrales múltiples 

import sympy as sp 
x, y = sp.symbols('x y') 

# Ejemplo para la práctica 3, ejercicio 9.a 
I1 = sp.integrate(1 + 2 * x + 2 * y, (y, 0, 1)) # resolvemos la integral más interna y la guardamos en I1. 
sp.simplify(sp.integrate(I1, (x, 0, 2))) # Ahora la más externa. Es importante aplicar el método simplify poque a veces puede quedar muy extensa. 

# Ejemplo para la práctica 3, ejercicio 9.b dX CON dY
I1 = sp.integrate(x + y, (x, y/2, 3))
sp.simplify(sp.integrate(I1, (y, 0, 6)))

#ej g
I1 = sp.integrate(x , (Z, 0, x*y))
sp.simplify(sp.integrate(I1, (y, 0, x)))

sp.simplify(sp.integrate(I2,(x,0,1)))

