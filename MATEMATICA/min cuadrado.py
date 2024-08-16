# -*- coding: utf-8 -*-

# Práctica 5 parte 4 Ej. 1.b 
import numpy as np 
import matplotlib.pyplot as plt 

x = np.array([1, 3, 5, 6, 7]) #valores de x o de m
Y = np.array([0.1, 2, 4, 5, 7]) #valores de Y mayuscula ojo o de b segun caso

plt.scatter(x, Y) 

A = np.vander(x, 2) #pinto solo a para formar matrix y ver las dos coulmnas de mi matriz

X = np.linalg.inv(np.transpose(A) @ A) @ np.transpose(A) @ Y 

#grafico extra sobre los puntos.incompleto
import matplotlib.pyplot as plt
import numpy as np
plt.title('Funcion original',color = "red") 
plt.axhline(0.2, color = "black")
plt.xlabel('Eje x') 



# Transformaciones: ejemplo del período de los planetas y su distancia al sol (Larson, Fundamentos de álgebra lineal, p268) 

import csv  #para leer/importar los archivos csv

file = open("MCuad.csv", "r") #"r" es por "read". No olvidemos especificar el directorio de trabajo. 
data = list(csv.reader(file, delimiter = ",")) # convertimos a lista.  separador coma , 
file.close() 
print(data) 
#vemos en la consolo el archivos con datos
x = [float(row[1]) for row in data[1:]]  #fila 1 con todas las columnas
Y = [float(row[2]) for row in data[1:]] 
plt.scatter(x, Y) # no parecen estar sobre una recta (más o menos) y hay puntos agrupados y otros separados. Tomamos, mejor, el logaritmo de cada coordenada. 

ln_x = np.log(x) 
ln_Y = np.log(Y) 

plt.scatter(ln_x, ln_Y) # parece que ahora sí mejora el grafico

A = np.vander(ln_x, 2)

X = np.linalg.inv(np.transpose(A) @ A) @ np.transpose(A) @ ln_Y 
X  #3obtengo pendiente y ordenada 
''' 
redondeamos a m = 3/2 y b = 0 
=> ln(y) = 3/2 * ln(x) 
y si destransformamos: 
y = x^(3/2) 
''' 


# Polinomio cuadrático de MC 

x = np.array([-2, -1, 0, 1, 2])
Y = np.array([0, 0, 1, 2, 5]) 

plt.scatter(x, Y) 

A = np.vander(x, 3)#agarra las 3 columnas

X = np.linalg.inv(np.transpose(A) @ A) @ np.transpose(A) @ Y 
X 

#ejmplo a1
import numpy as np 
import matplotlib.pyplot as plt 

x = np.array([0, 1, 2, 3, 4]) #valores de x o de m
Y = np.array([0.1,1.1,2.4,2.9,4.7]) #valores de Y mayuscula ojo o de b segun caso

plt.scatter(x, Y) 

A = np.vander(x, 2) #pinto solo a para formar matrix y ver

X = np.linalg.inv(np.transpose(A) @ A) @ np.transpose(A) @ Y 

#grafico 5
import numpy as np 
import matplotlib.pyplot as plt 

x = np.array([1,5,10,20]) #valores de x o de m
Y = np.array([1.5,2.069,2.37,2.73]) #valores de Y mayuscula ojo o de b segun caso

plt.scatter(x, Y) 

A = np.vander(x, 2) #pinto solo a para formar matrix y ver

X = np.linalg.inv(np.transpose(A) @ A) @ np.transpose(A) @ Y 
ln_x = np.log(x) 
ln_Y = np.log(Y) 

plt.scatter(ln_x, ln_Y) # parece que ahora sí mejora el grafico

A = np.vander(ln_x, 2)

X = np.linalg.inv(np.transpose(A) @ A) @ np.transpose(A) @ ln_Y 
X  #3obtengo pendiente y ordenada 

