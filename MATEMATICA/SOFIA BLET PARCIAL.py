#ej 1 grafico tridimencional de la superficie
import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, np.pi*2, 100) # Valores en x en el grafico 
y = np.linspace(0, np.pi*2, 100) # Valores en y 
X, Y = np.meshgrid(x, y) # Creamos la grilla
Z = np.sin(X) + np.cos(Y)

# Crear figura y ejes 3D. Todo esto correrlo junto. 
fig = plt.figure() # Abre una figura vacía. 
ax = fig.add_subplot(111, projection = '3d') 
surf = ax.plot_surface(X, Y, Z) # Graficar superficie
plt.gca().mouse_init() # Activamos la herramienta de rotación interactiva. 
ax.set_xlabel('Eje X') # Etiqueta eje x 
ax.set_ylabel('Eje Y') # Etiqueta eje y 
ax.set_zlabel('Eje Z') # Etiqueta eje z 
plt.show()

#ej 2  curvas de nivel entre 10 y 20,elijo 15
fig, ax = plt.subplots()
cnt = ax.contour(X, Y, Z, levels = 15) # Creamos las curvas de nivel.
ax.clabel(cnt, cnt.levels, inline = True, fontsize = 10) # Mostramos directamente en el gráfico cuál es cada nivel de z. 
plt.show()

#Ej 3 
from sympy import symbols, diff, sqrt 
import numpy as np 
# Definir las variables simbólicas
x, y = symbols('x y')

# Definir i y j 
i = np.array([1, 0]) 
j = np.array([0, 1]) 

# Definir la función
f =np.sin(X) + np.cos(Y)

# Definir el punto en el que se evalúa la derivada direccional
x0 =np.pi
y0 = np.pi/2

# Definir la dirección del vector 
u = np.array([1, -1]) 

# Calcular el gradiente de la función evaluado en el punto 
f_x = diff(f, x) 
f_y = diff(f, y) 
f_x = f_x.subs(x, x0) 
f_y = f_y.subs(y, y0) 

gradiente_en_P = f_x * i + f_y * j 

# Calcular la norma de u y normalizarlo 
norm_u = sqrt(u[1]**2 + u[-1]**2) #entre corchetes va el valor que quiero,desde cero a x
u_normalizado = u / norm_u 

# Calcular la derivada direccional 
np.dot(gradiente_en_P, u_normalizado) 

#La derivada direccional es la pendiente de la supercicie y nos da 0 eso significa que
#el mínimo local será nula, al obtener el valor cero si se multiplica el vector gradiente, nulo, por cualquier otro vector me sigue dando 0
#Como toda derivada es la razón de cambio resultante en la salida de la función.
#Así que si multiplico el vector ‍ por dos duplicaría el valor de la derivada direccional, ya que todos los cambios ocurrirían el doble de rápido.

