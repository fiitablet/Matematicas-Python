#EJERCICIO 2
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp 

def f(t,Z): 
    N1, N2 = Z   
    dN1dt =10*N1*(50 - N1 - 2*N2)/50 #1er ecuacion
    dN2dt = 10*N2*(30 - N1 - N2)/30  #2da ecuacion
    return [dN1dt, dN2dt]
#Las especie N1 y N2 van a competir por los mismos recursos/por sobrevivir,pueden ser ambos presa o ambos depredadores
Z0 = [150, 150] #Ambas especie tiene como condicion inicial 150 individuos
 

t_eval = np.arange(0,5, 0.1)#tiempo de 0 a 5 como ejemplo,no importa el tiempo elegido.Analizar grafico para que pasa a largo plazo
sol = solve_ivp(f, [0, 5], Z0, t_eval = t_eval)
#Grafico en funcion del tiempo
plt.plot(sol.t, sol.y[0], label = "Especie 1") 
plt.plot(sol.t, sol.y[1], label = "Especie 2") 
plt.legend() 
#Campo de direcciones en funcion de las diferentes especies
plt.plot(sol.y[0], sol.y[1]) 
N1,N2 = np.meshgrid(np.arange(0,150, 5), np.arange(0, 150,5)) #donde termina "x" e "y" en el eje
u = 10*N1*(50 - N1 - 2*N2)/50  #1er ecuacion 
v = 10*N2*(30 - N1 - N2)/30 #2da ecuacion
n = np.sqrt(u**2 + v**2) # Normalizamos el vector 
plt.quiver(N1, N2, u/n, v/n)

#plt.xlim(0, 40) 
#plt.ylim(0, 40) 
plt.title('Relacion entre la especie 1  y la especie 2 ',color = "purple") 
plt.show() 

""" Conlcusion con condicion inicial 150 de ambas especies:
La especie 1 gana la competencia sobre la especie 2,vemos en los graficos que
la especie 1 tiene una zona donde empieza a resuperarse luego de disminuir junto
con la especie 2  y esta seahace constante(sin cambio).
la otra especie 2 comienza a disminuir hasta su extincion y su valor sea 0 
Queda: 50 especie 1 VS 0 especie 2 """


#Otra condicion inicial,item c
Z0=[50,50]

t_eval = np.arange(0,3, 0.1)#tiempo de 0 a 3 como ejemplo,no importa el tiempo elegido.Analizar grafico para que pasa a largo plazo
sol = solve_ivp(f, [0, 3], Z0, t_eval = t_eval)
#Grafico en funcion del tiempo
plt.plot(sol.t, sol.y[0], label = "Especie 1") 
plt.plot(sol.t, sol.y[1], label = "Especie 2") 
plt.legend() 
#Campo de direcciones  en funcion de las diferentes especies
plt.plot(sol.y[0], sol.y[1]) 
N1,N2 = np.meshgrid(np.arange(0,80, 3), np.arange(0, 80,3)) #donde termina "x" e "y" en el eje
u = 10*N1*(50 - N1 - 2*N2)/50  #1er ecuacion 
v = 10*N2*(30 - N1 - N2)/30 #2da ecuacion
n = np.sqrt(u**2 + v**2) # Normalizamos el vector 
plt.quiver(N1, N2, u/n, v/n)

#plt.xlim(0, 40) 
#plt.ylim(0, 40) 
plt.title('Relacion especie 1 y 2 ',color = "purple") 
plt.show() 


""" Conclusion con condicion inicial 50 de ambas especies:
La especie 2 disminuye al igual que en el otro caso,pero la especie 1 cuando disminuye 
luego comienza a crecer muy fuertemente hasta ganar
Queda:50 especie 1  vs 0 especie 2
  """

