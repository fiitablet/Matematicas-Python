import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp 

def f(t,Z): 
    N1, N2 = Z   
    dN1dt =r1*N1*(K1-N1-alfa*N2)/K1 #1er ecuacion
    dN2dt = r2*N2*(k2 - N2 - beta*N1)/k2 #2da ecuacion
    return [dN1dt, dN2dt]
Z0=[10,10]
r1=1
r2=1
alfa=1
beta=1
K1=1
k2=1
 
t_eval = np.arange(0,5, 0.1)#tiempo de 0 a 5 
sol = solve_ivp(f, [0, 5], Z0, t_eval = t_eval)
#Grafico en funcion del tiempo
plt.plot(sol.t, sol.y[0], label = "Especie 1") #especie 1 y 2
plt.plot(sol.t, sol.y[1], label = "Especie 2") 
plt.legend() 
#Campo de direcciones en funcion de las diferentes especies
plt.plot(sol.y[0], sol.y[1]) 
N1,N2 = np.meshgrid(np.arange(0,10, 0.2), np.arange(0, 10,0.2)) #donde termina "x" e "y" en el eje
u = r1*N1*(K1-N1-alfa*N2)/K1 #1er ecuacion 
v = r2*N2*(k2 - N2 - beta*N1)/k2 #2da ecuacion
n = np.sqrt(u**2 + v**2) # Normalizamos el vector 
plt.quiver(N1, N2, u/n, v/n)

#plt.xlim(0, 40) 
#plt.ylim(0, 40) 
plt.title('Relacion especie 1 y 2 ',color = "purple") 
plt.show() 
