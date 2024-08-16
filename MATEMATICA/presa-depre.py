# Presa - depredador 
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp 

def f(t, y): 
    P, D = y  #le doy condi inicial 
    dPdt = a * P - c * P * D #modi
    dDdt = l * D * P - k * D #modificar
    return [dPdt, dDdt]

a = 1.2 #modif todo
c = 0.9 
l = 0.8 
k = 0.6 

y0 = [3, 2] #valor inicial 3 presa 2 depredador mofdif
t_eval = np.arange(0, 20.1, 0.1) #0.1 separacion unidades modif
sol = solve_ivp(f, [0, 20], y0, t_eval = t_eval) 
#junto para el grafuico
plt.plot(sol.t, sol.y[0], label = "Presas") #especie 1 y 2 cambiar nombre
plt.plot(sol.t, sol.y[1], label = "Depredadores") 
plt.legend() 
 #todo junto
plt.plot(sol.y[0], sol.y[1]) 
x, y = np.meshgrid(np.arange(0, 4.3, 0.3), np.arange(0, 4.3, 0.3)) #grilla de valores separados
u = 1.2 * x - 0.9 * x * y  #valores de a b y c y k  ec presa y modif ec
v = - 0.6 * y + 0.8 * x * y #ecuacion depre modif
n = np.sqrt(u**2 + v**2) # Normalizamos el vector 
plt.quiver(x, y, u/n, v/n)
plt.xlim(0, 4) 
plt.ylim(0, 4.5) 
plt.show() 


"""                          sigo ej"""

#ej 1 pratica 6 3
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp 

def f(t,Z): 
    Y, X = Z  #le doy condi inicial 
    dYdt = a *X + b * Y
    dXdt = alfa * X +be *Y
    return [dYdt, dXdt]

a = -4 #modif todo
b = -1
alfa = 2 
be =-1

Z0 = [10, 10]
t_eval = np.arange(0, 20.1, 0.1)
sol = solve_ivp(f, [0, 20], Z0, t_eval = t_eval) 
#junto ora el grafuico
plt.plot(sol.t, sol.y[0], label = "Especie x") #especie 1 y 2 cambiar nombre
plt.plot(sol.t, sol.y[1], label = "Especie y") 
plt.legend() 
 #todo junto
plt.plot(sol.y[0], sol.y[1]) 
x, y = np.meshgrid(np.arange(-40,40, 0.3), np.arange(-40, 40,0.3)) #grilla de valores separados
u = -4*x +(-1)*y  #valores de a b y c y k  ec presa y modif ec
v = 2*x+(-1)*y #ecuacion depre modif
n = np.sqrt(u**2 + v**2) # Normalizamos el vector 
plt.quiver(x, y, u/n, v/n)

plt.xlim(0, 40) 
plt.ylim(0, 40) 
plt.show() 

#tp 4 
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp 

def f(t,Z): 
    A, B = Z  #le doy condi inicial 
    dAdt = 3.5*𝐴 *(1-𝐴/200)-0.2 *𝐴 *𝐵 
    dBdt = 0.04*𝐴 *𝐵 - 1.2 *𝐵
    return [dAdt, dBdt]

Z0 = [150, 20]#condi inicial presas y depre
Z0=[430,15] #otra situacion ojoo q puede ser z1 y despues invoco con z1


t_eval = np.arange(0,70, 0.1)#tiempo de 0 a 70
sol = solve_ivp(f, [0, 70], Z0, t_eval = t_eval) #tiempo evaluacion ojo
#junto ora el grafuico
plt.plot(sol.t, sol.y[0], label = "Especie PRESA") #especie 1 y 2 cambiar nombre
plt.plot(sol.t, sol.y[1], label = "Especie DEPREDADOR") 
plt.legend() 
 #todo junto
plt.plot(sol.y[0], sol.y[1]) 
A,B = np.meshgrid(np.arange(0,180, 4), np.arange(0, 50,4)) #grilla de valores separados
u = 3.5*𝐴 *(1-𝐴/200)-0.2 *𝐴 *𝐵  #valores de a b y c y k  ec presa y modif ec
v =  0.04*𝐴 *𝐵 - 1.2 *𝐵 #ecuacion depre modif
n = np.sqrt(u**2 + v**2) # Normalizamos el vector 
plt.quiver(A, B, u/n, v/n)

#plt.xlim(0, 40) 
#plt.ylim(0, 40) 
plt.show() 