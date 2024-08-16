import sympy as sp
x, y = sp.symbols('x y')
sp.integrate(sp.sin(x**2), (x, 0, 3.14)) # integral definida entre 0 y Pi(3.14)
#NOS DA UNA COSA RARA,GRAFICAMOS Y ELEGIMOS UN METODO ADECUADO 

#graficamos para ver si hay curvas encima del eje x,seleccionar todo el bloque de codigo 
import matplotlib.pyplot as plt
import numpy as np
x = np.arange(-5,5,0.05)
y = np.sin(x**2)
plt.plot(x, y)
plt.title('Funcion original sin(x**2)',color = "red") 
plt.axhline(0.2, color = "black")
plt.xlabel('Eje x') 

#hacemos un zoom al grafico 
import mpmath
mpmath.plot(lambda x: mpmath.sin(x**2), [0, 3.14])


#pruebo metodo de trapecios para hayar la integral
import numpy as np 

def f(x): return  np.sin(x**2)

def ej2(h): 
    a = 0 # valor x de mi intervalo
    b = 3.14 #valor y de mi intervalo
    n = int((b - a) / h) 
    S = 0 # suma  
    for i in range(n): 
        xmin = a + i * h 
        xmax = a + (i + 1) * h 
        yizq = f(xmin) 
        yder = f(xmax) 
        S = S + (yizq + yder) / 2 * h #segmento superior del trapecio es lineal, es lo mismo calcular el punto medio como una altura media y hacer la fórmula del área del rectángulo con base h y altura (yizq + yder) / 2 
    return(S) 

ej2(0.0001)  

#grafico con relleno

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 1000)
y = 2 * x 

plt.plot(x, y)
plt.fill_between(x, y, color = 'grey', alpha = 0.5)
plt.show()





