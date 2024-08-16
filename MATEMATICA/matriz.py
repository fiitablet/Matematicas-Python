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

# Matrices en bloque
A = np.array([[1, 3, 2], 
              [1, 0, 0], 
              [1, 2, 2]]) 

B = np.arange(1, 10).reshape(3, 3) # Otra forma de definir la matriz  3x3 COPIO TODOS LO DE ADENTRO (1,3,2,2,2,2,1,2,2,)

A + B 
A - B 
2 * A # Producto por un escalar 
A.shape # Dimensión de la matriz 
np.dot(A, B) # Multiplicación de matrices 
A @ B # Otra forma de escirbir multipliacion
np.eye(3) # Matriz identidad 3x3 
np.linalg.det(A) # Determinante de A
np.linalg.inv(A)  # Matriz inversa  A* a a la -1=I
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

b = np.array([6, 4, 2]).reshape(3, 1) # Matriz de resultados  de la derecha

X = np.linalg.solve(A, b) # Usando la función solve de np.linalg 
X 
X = np.linalg.inv(A) @ b # Haciéndolo "a mano" 
X 

# Autovalores y autovectores 

A = np.array([[3, 2, -1], [2, 3, 1], [0, 0, 5]])
aval, avec = np.linalg.eig(A)
aval 
avec 

#ejemplo 3 guia 4 pt2
A = np.array([[1, 0, 0], 
              [2, -1, 3], 
              [0, 0, 1]]) 

np.linalg.inv(A) #este caso da =

A = np.array([[1, 1, 1], 
              [1, 2, 2], 
              [1, 2, 3]]) 

np.linalg.inv(A)
#4)2 tarea 
''' 
3x  + 5y + z = -2
x  + z = -2
-6x + 3y  = 0
''' 
A = np.array([[3, 5, 1], 
             [1, 0, 1], 
             [-6, 3, 0]]) # Matriz de coeficientes 
b = np.array([-2, -2, 0]).reshape(3, 1) # resultados derecha
X = np.linalg.solve(A, b) #llamo a x en la consola
X
np.linalg.inv(A)  #VEO INVERSA
