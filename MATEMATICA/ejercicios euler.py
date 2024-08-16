# -*- coding: utf-8 -*-
"""
y′ = 3 − 2y 
ej 11a


"""
#campo de direcciones
import matplotlib.pyplot as plt
import numpy as np
#-10min  10max 1 el paso/dist
t, y = np.meshgrid(np.arange(-10, 10, 1), np.arange(-2, 5, 0.5)) #creo una grilla bidireccional t y
u = 3 - 2*y # siempre despejar y' 
n = np.sqrt(u**2 + 1**2) 
plt.quiver(t, y, 1/n, u/n)
plt.xlim(-10, 10)
plt.ylim(-3, 6)
plt.show() 

#ejemplo j
t, y = np.meshgrid(np.arange(-10, 10, 1), np.arange(-10, 10, 1)) #creo una grilla bidireccional t y
u = y**2-t * y # siempre despejar y' 
n = np.sqrt(u**2 + 1**2) 
plt.quiver(t, y, 1/n, u/n)
plt.xlim(-10, 10)
plt.ylim(-10, 10)
plt.show() 



