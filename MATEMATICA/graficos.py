# -*- coding: utf-8 -*-
"""
                        COMO GRAFICAR 1 O + FUNCIONES 
"""
import matplotlib.pyplot as plt #biblioteca de visualizacion
import numpy as np 

x = np.arange(-3, 3, 0.1)  #crea un arreglo de valores de x que van desde -3 hasta justo antes de 3 con un paso de 0.1.
#Estos valores de x se utilizan para evaluar las funciones f(x) y g(x).

#Funciones a graficar
f = (x**2-x-6)/(x**2-2) # aca la fc ori
g =-2*x**5-24*x**4-8*x**3+32*x**2+24*x+32/(x**2-2)**4 #aca la derivada segunda 


plt.plot(x, f)  #grafico f respecto de x
plt.plot(x, g)  #grafico g
plt.xlim(-3, -1) # los limites max y min del eje x, se va a graficar en x desde el -3 al 3
plt.ylim(-20, 15) # Límite en y, pueden no escribirlo si quieren
plt.axhline(0, color = "black") # pinto el Eje x de color negro
plt.axvline(0, color = "black") # Eje y  









