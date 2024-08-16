

import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


# Matrices 

A = np.array([[1, 3, 2], 
              [1, 0, 0], 
              [1, 2, 2]]) 

B = np.arange(1, 10).reshape(3, 3) # Otra forma de definir la matriz B seria otra matriz

A + B 
A - B 
2 * A # Producto por un escalar 
A.shape # Dimensión de la matriz 
np.dot(A, B) # Multiplicación de matrices 
A @ B # Otra forma de multiplicar 
np.eye(3) # Matriz identidad 3x3 
np.linalg.det(A) # Determinante 
np.linalg.inv(A)  # Matriz inversa 
np.transpose(A) # Matriz transpuesta 

# Método matricial de resolución de sistemas de ecuaciones lineales 
''' 
x  + 2y + 3z = 6
2x + 5y + 2z = 4
6x − 3y + z  = 2 
''' 

A = np.array([[1, 2, 3], 
             [2, 5, 2], 
             [6, -3, 1]]) # Matriz de coeficientes 

b = np.array([6, 4, 2]).reshape(3, 1) # Matriz de resultados 

X = np.linalg.solve(A, b) # Usando la función solve de np.linalg 
X 
X = np.linalg.inv(A) @ b # Haciéndolo "a mano" 
X 



# Álgebra lineal - vectores 

import numpy as np

v1 = np.array([1, -3, 12.4]) # Usamos la función array. 
v2 = np.arange(-2, 4, 2) # Usamos la función arange. 
v3 = np.zeros(5) # vector sólo de ceros. 
v4 = np.ones(3) # vector de sólo unos. 

v1 + v2 # Suma de vectores 
v1 - v2 # Resta de vectores 
2 * v1 # Producto por un escalar 
np.dot(v1, v2) # Producto escalar o producto punto 
v1 @ v2 # Otra forma de calcular el producto punto 
np.cross(v1, v2) # Producto vectorial o producto cruz 
np.linalg.norm(v1) # Norma del vector 


def graficarVectores(vecs, cols, alpha = 1):
    plt.figure()
    plt.axvline(x = 0, color = 'grey', zorder = 0) # zorder es el orden en el eje z (en un gráfico 2D se entiende como el orden de las capas). 
    plt.axhline(y = 0, color='grey', zorder = 0)
    for i in range(len(vecs)): 
        x = np.concatenate([[0, 0], vecs[i]])
        plt.quiver([x[0]], # quiver muestra los vectores como flechas 
                   [x[1]],
                   [x[2]],
                   [x[3]],
                   angles = 'xy', scale_units = 'xy', scale = 1, color = cols[i], alpha = alpha)


v1 = np.array([2, 5])
v2 = np.array([3, 2])
v1v2 = 2 * v1 + 1 * v2
v1v2

graficarVectores([v1, v2, v1v2], ['orange', 'blue', 'red'])
plt.xlim(-1,8)
plt.ylim(-1,13) 



# Combinación lineal 

c1, c2, c3 = sp.symbols('c1 c2 c3')
f = sp.Eq(-c2 + 3*c3, -1)
g = sp.Eq(c1 + c2 + c3, -2)
h = sp.Eq(4*c1 + 2*c2 + 2*c3, -2)
sp.solve([f, g, h], (c1, c2, c3))



# Autovalores y autovectores 

A = np.array([[3, 2, -1], [2, 3, 1], [0, 0, 5]])
aval, avec = np.linalg.eig(A) #me da los autovalores para chequearlos 
aval 
avec 




