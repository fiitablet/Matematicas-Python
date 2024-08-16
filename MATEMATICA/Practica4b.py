import math 

def sucesion(cant_term): 
    s = [] # creamos una lista vacía 
    for n in range(1, cant_term + 1) :
        valor_term = 3**n 
        s.append(valor_term) # append agrega un elemento a la lista s 
    return s 

sucesion(4) 

#%%
def serie(k):
    S = 0 # inicializamos la variable donde vamos a ir sumando 
    for n in range(1,k+1): # evaluo de 1 a k (recordar que el range va de 1 a k-1, por eso le sumo 1)
        s = 1 / (n**2 + 1) # sucesión 
        S = S + s # suma de cada punto de la sucesion
    return S

serie(1000) #sucesion de 1 a 10000
math.pi/4 #a donde converge la integral

#%%        
n= 3
math.factorial(n) #factorial n
math.pi
math.sqrt(n)
math.e #numero e
math.exp(n) #e**n