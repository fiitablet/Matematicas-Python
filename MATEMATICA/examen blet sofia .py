#calculo limites 
from sympy import limit, oo, Symbol
x = Symbol('x') # declaramos la variable simbólica
y=(x+5)**0.5/(x-2)**3
limit(y, x, oo) # Límite en el infinito
limit(y, x, -oo) # Límite en el menos infinito
#rta ambos limites nos dan CERO

#ahora busco la 1er derivada
import sympy as sp
x = sp.Symbol('x')
y =(x+5)**0.5/(x-2)**3 #pase la funcion a potencia
y=sp.sqrt(x+5)/(x-2)**3 # otra forma de escribir usando sqrt para la raiz ,termina dando los mismo
sp.diff(y, x) #1er derivada
sp.diff(y, x, x) # derivada segunda
#rta 1er derivada --> 0.5/((x - 2)**3*(x + 5)**0.5) - 3*(x + 5)**0.5/(x - 2)**4 o bien 1/(2*(x - 2)**3*sqrt(x + 5)) - 3*sqrt(x + 5)/(x - 2)**4
#rta 2da derivada--> (-0.25/(x + 5)**1.5 - 3.0/((x - 2)*(x + 5)**0.5) + 12*(x + 5)**0.5/(x - 2)**2)/(x - 2)**3

#grafico 
import matplotlib.pyplot as plt 
import numpy as np 
x = np.arange(-3,3,0.1)  #arreglo desde -3 hasta justo antes de 3 con un paso de 0.1.
f=(x+5)**0.5/(x-2)**3 # aca la fc ori 
plt.plot(x, f)  #grafico f respecto de x

plt.xlim(-3, -3) # los limites max y min del eje x, se va a graficar en x desde el -3 al 3
plt.ylim(-20, 15) # Límite en y, pueden no escribirse
plt.axhline(0, color = "black") # pinto el Eje x de color negro
plt.axvline(0, color = "black") # Eje y  
plt.title(' No me salio el grafico ',color = "red")

#integral
import sympy as sp 
x, y = sp.symbols('x y')
(sp.integrate(x+1)/(x**3), (x, 0.5, 2.5)) # integral definida evaluo

#pruebo metodo de trapecios para hayar la integral
import numpy as np 
def f(x): return  (x+1)/(x**3)
def integral(h): 
    a = 0.5 # valor x de mi intervalo
    b = 2.5#valor y de mi intervalo
    n = int((b - a) / h) 
    S = 0 
    for i in range(n): 
        xmin = a + i * h 
        xmax = a + (i + 1) * h 
        yizq = f(xmin) 
        yder = f(xmax) 
        S = S + (yizq + yder) / 2 * h #segmento superior del trapecio es lineal, es lo mismo calcular el punto medio como una altura media y hacer la fórmula del área del rectángulo con base h y altura (yizq + yder) / 2 
    return(S) 

integral(0.0001)  













