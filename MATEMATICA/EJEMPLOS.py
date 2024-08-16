"ejemplo 3g"
import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


# Matrices 

A = np.array([[-0.4, 0.4, 0.3], 
              [0.2, 0.2, 0.2], 
              [0.3, 0.2, 0.2]]) 

B = np.arange(1, 10).reshape(3, 3) # Otra forma de definir la matriz 

A@B #sirve para multiplicar 
A + B 
A - B 
2 * A # Producto por un escalar 
A.shape # Dimensión de la matriz 
np.dot(A, B) # Multiplicación de matrices l
np.eye(3) # Matriz identidad 3x3 
np.linalg.det(A) # Determinante 
np.linalg.inv(A)  # Matriz inversa 
np.transpose(A) # Matriz transpuesta 
np.trace(A) #TRAZA


A = np.array([[1, 1, -3], 
             [-1, 2, 0], 
             [1, -1, 1]]) # Matriz de coeficientes 

b = np.array([-1, 1, 2]).reshape(3, 1) # Matriz con los resultados 

X = np.linalg.solve(A, b) # Usando la función solve de np.linalg 
X 
X = np.linalg.inv(A) @ b # Haciéndolo "a mano" 
X 


A = np.array([[-3,-2,-3], [-3, -4, 9], [-1, -2, 5]])
aval, avec = np.linalg.eig(A) #me da los autovalores para chequearlos de AUTOVECTOR
aval 
avec 




import sympy as sp 
x, y = sp.symbols('x y') 

# Ejemplo para la práctica 3, ejercicio 9.a 
I1 = sp.integrate(x**2*y**2, (x, 0.5*y, y**0.5)) # resolvemos la integral más interna y la guardamos en I1. 
sp.simplify(sp.integrate(I1, (y, 0, 4))) # Ahora la más externa. Es importante aplicar el método simplify poque a veces puede quedar muy extensa.


