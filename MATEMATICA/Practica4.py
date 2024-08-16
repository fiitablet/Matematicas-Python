import math 

def sucesion(cant_term): 
    s = [] # creamos una lista vacía 
    for n in range(1, cant_term + 1) :
        valor_term = math.cos(1/n) 
        s.append(valor_term) # append agrega un elemento a la lista s 
    return s 

sucesion(20) 


def serie(k):
    S = 0 # inicializamos la variable donde vamos a ir sumando 
    for n in range(1,k+1): # evaluo de 1 a k (recordar que el range va de 1 a k-1, por eso le sumo 1)
        s = 1 / (n**2 + 1) # sucesión 
        S = S + s # suma de cada punto de la sucesion
    return S

serie(1000) #sucesion de 1 a 10000 

a = [1, 2] 
a[0] 


def fibonacci(cant_term): 
    s = [1, 1] # Condiciones iniciales 
    for n in range(2, cant_term + 1) :
        valor_term = s[n-2] + s[n-1] 
        s.append(valor_term) 
    return s 

fibonacci(10) 


def no_homog(cant_term): 
    s = [12, 0] # Condiciones iniciales 
    for n in range(2, cant_term + 1) :
        valor_term = 4 * s[n-1] - 3 * s[n-2] + 36 * (n-1)**2 
        s.append(valor_term) 
    return s 

no_homog(10) 








