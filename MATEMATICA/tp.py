# 1)a) la ecuacion A es presa y la B es depredador
#b)
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp 

# Campo de direcciones 

a = 5
b = -0.2
c = -3
d = 0.1 

x1, x2 = np.meshgrid(np.arange(-3, 32, 1), np.arange(-3, 32,1)) #creo la grilla
u = a * x1 + b * x1 *x2  #esto se cambia OJO X1 ES A Y X2 ES B signos NO SE TOCA
v = c * x2 + d * x1 *x2 # aca tb     
n = np.sqrt(u**2 + v**2) # Normalizamos el vector 
plt.figure() 
plt.quiver(x1, x2, u/n, v/n) 
plt.axhline(0, color = "black") 
plt.axvline(0, color = "black") 
plt.show() 

# Serie de tiempo 

def f(t, x): 
    x1, x2 = x 
    dx1dt =a* x1 + b * x1 *x2 
    dx2dt = c * x2 + d * x1 *x2
    return [dx1dt, dx2dt]

a = 5
b = -0.2
c = -3
d = 0.1 

x0 = [65, 30] #ci
t_eval = np.arange(0, 5, 0.01)
sol = solve_ivp(f, [0, 5], x0, t_eval = t_eval) #0 5 rango
#todo la linea
plt.figure() 
plt.plot(sol.t, sol.y[0], label = "x1(PRESA)") 
plt.plot(sol.t, sol.y[1], label = "x2(DEPREDADOR)") 
plt.legend() 


# Campo de direcciones con trayectoria 

plt.figure() 
plt.plot(sol.y[0], sol.y[1]) 
x1, x2 = np.meshgrid(np.arange(0, 80, 5), np.arange(0, 80, 5)) #cambio el 80 y eñ rago si quiero
u = a * x1 + b * x1 *x2  #esto se cambia pero no los signos
v = c * x2 + d * x1* x2 #aca tb
n = np.sqrt(u**2 + v**2) # Normalizamos el vector 
plt.quiver(x1, x2, u/n, v/n)
plt.axhline(0, color = "black") 
plt.axvline(0, color = "black") 
plt.xlim(-3, 80) 
plt.ylim(-3, 80) 
plt.show() 


# Campo de direcciones con isoclinas 

plt.figure() 
x1, x2 = np.meshgrid(np.arange(-3, 33, 1), np.arange(-3, 33, 1))
u = a * x1 + b * x1* x2 
v = c * x2 + d * x1* x2 
n = np.sqrt(u**2 + v**2) # Normalizamos el vector 
plt.quiver(x1, x2, u/n, v/n)
plt.plot(x1[0], 1* x1[0], color = "red") # Isoclina x1 el -1/2 es despejado de k2
plt.plot(x1[0], 1 * x1[0], color = "gray") # Isoclina x2 despejo k2 y me da 4 ojo los signos
plt.axhline(0, color = "black") 
plt.axvline(0, color = "black") 
plt.xlim(-3, 40) 
plt.ylim(-3,40) 
plt.show() 

#ejercicio 2 

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp 

# Campo de direcciones 

a = 5
b = -0.2
c = -3
d = 0.1 
e=75 #nuevo parametro a considerar y se divide

x1, x2 = np.meshgrid(np.arange(-3, 28, 1), np.arange(-3, 28,1)) #creo la grilla
u = a * x1*(1-x1/e) + b * x1 *x2  #esto se cambia
v = c * x2 + d * x1 *x2 # aca tb
n = np.sqrt(u**2 + v**2) # Normalizamos el vector 
plt.figure() 
plt.quiver(x1, x2, u/n, v/n) 
plt.axhline(0, color = "black") 
plt.axvline(0, color = "black") 
plt.show() 
#todo lo anterior era para declarar la nueva variable e ,el grafico sigue dando lo mismo
# Serie de tiempo 

def f(t, x): 
    x1, x2 = x 
    dx1dt =a * x1*(1-x1/e) + b * x1 *x2
    dx2dt = c * x2 + d * x1 *x2
    return [dx1dt, dx2dt]

a = 5
b = -0.2
c = -3
d = 0.1 

x0 = [65, 30] #ci dice la consigna que se mantiene igual al pto anterior 
t_eval = np.arange(0, 5, 0.01)
sol = solve_ivp(f, [0, 5], x0, t_eval = t_eval) #0 5 rango
#todo la linea
plt.figure() 
plt.plot(sol.t, sol.y[0], label = "x1(PRESA)") 
plt.plot(sol.t, sol.y[1], label = "x2(DEPREDADOR)") 
plt.legend() 


# Campo de direcciones con trayectoria 

plt.figure() 
plt.plot(sol.y[0], sol.y[1]) 
x1, x2 = np.meshgrid(np.arange(0, 80, 5), np.arange(0, 80, 5))
u = a * x1*(1-x1/e) + b * x1 *x2  #esto se cambia pero no los signos
v = c * x2 + d * x1* x2 #aca tb
n = np.sqrt(u**2 + v**2) # Normalizamos el vector 
plt.quiver(x1, x2, u/n, v/n)
plt.axhline(0, color = "black") 
plt.axvline(0, color = "black") 
plt.xlim(-3, 80) 
plt.ylim(-3, 80) 
plt.show() 


# Campo de direcciones con isoclinas 

plt.figure() 
x1, x2 = np.meshgrid(np.arange(-3, 33, 1), np.arange(-3, 33, 1))
u = a * x1*(1-x1/e) + b * x1 *x2
v = c * x2 + d * x1* x2 
n = np.sqrt(u**2 + v**2) # Normalizamos el vector 
plt.quiver(x1, x2, u/n, v/n)
plt.plot(x1[0], 1* x1[0], color = "red") # Isoclina x1 el -1/2 es despejado de k2
plt.plot(x1[0], 1 * x1[0], color = "gray") # Isoclina x2 despejo k2 y me da 4 ojo los signos
plt.axhline(0, color = "black") 
plt.axvline(0, color = "black") 
plt.xlim(-3, 40) 
plt.ylim(-3,40) 
plt.show() 

#ejercicio 2 












