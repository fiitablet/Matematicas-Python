import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp 

''' Tomemos como ejemplo 
x1' = x1 + 2*x2 
x2' = 4x1 - x2 
'''

# Campo de direcciones 

a = 1
b = 2
c = 4
d = -1 
#como el metodo euler solo cambian las variables
x1, x2 = np.meshgrid(np.arange(-3, 3, 0.25), np.arange(-3, 3, 0.25)) #creo la grilla
u = a * x1 + b * x2  #esto se cambia
v = c * x1 + d * x2 # aca tb
n = np.sqrt(u**2 + v**2) # Normalizamos el vector 
plt.figure() 
plt.quiver(x1, x2, u/n, v/n)
plt.axhline(0, color = "black") 
plt.axvline(0, color = "black") 
plt.show() 

# Serie de tiempo 

def f(t, x): 
    x1, x2 = x 
    dx1dt = a * x1 + b * x2 
    dx2dt = c * x1 + d * x2 
    return [dx1dt, dx2dt]

a = 1
b = 2
c = 4
d = -1 

x0 = [1.5, -2.5] #ci
t_eval = np.arange(0, 1.3, 0.01)
sol = solve_ivp(f, [0, 5], x0, t_eval = t_eval) #0 5 rango
#todo la linea
plt.figure() 
plt.plot(sol.t, sol.y[0], label = "x1") 
plt.plot(sol.t, sol.y[1], label = "x2") 
plt.legend() 


# Campo de direcciones con trayectoria 

plt.figure() 
plt.plot(sol.y[0], sol.y[1]) 
x1, x2 = np.meshgrid(np.arange(-3, 3, 0.25), np.arange(-3, 3, 0.25))
u = a * x1 + b * x2  #esto se cambia pero no los signos
v = c * x1 + d * x2 #aca tb
n = np.sqrt(u**2 + v**2) # Normalizamos el vector 
plt.quiver(x1, x2, u/n, v/n)
plt.axhline(0, color = "black") 
plt.axvline(0, color = "black") 
plt.xlim(-3, 3) 
plt.ylim(-3, 3) 
plt.show() 


# Campo de direcciones con isoclinas 

plt.figure() 
x1, x2 = np.meshgrid(np.arange(-3, 3, 0.25), np.arange(-3, 3, 0.25))
u = a * x1 + b * x2 
v = c * x1 + d * x2 
n = np.sqrt(u**2 + v**2) # Normalizamos el vector 
plt.quiver(x1, x2, u/n, v/n)
plt.plot(x1[0], - 1/2 * x1[0], color = "red") # Isoclina x1 el -1/2 es despejado de k2
plt.plot(x1[0], 4 * x1[0], color = "gray") # Isoclina x2 despejo k2 y me da 4 ojo los signos
plt.axhline(0, color = "black") 
plt.axvline(0, color = "black") 
plt.xlim(-3, 3) 
plt.ylim(-3, 3) 
plt.show() 



