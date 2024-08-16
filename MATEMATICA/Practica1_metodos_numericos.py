
ciclo = 0 
for num in range(4, 8): 
    print(num) 
    ciclo = ciclo + 1 


# Ejercicio: usar un bucle for para calcular la suma de los primeros 100 números naturales (problema de Gauss) 

# Fórmula a la que llegó Gauss: 
100 * 101 / 2 

# Ejercicio: Usar un ciclo for para encontrar el factorial de 10. El factorial de un número se obtiene multiplicando todos los números enteros positivos que hay entre el 1 y ese número. 

#%% 
# Métodos numéricos para aproximar una integral definida: 

# Suma de Riemann 


def f(x): 
    return (x**2) 

def ej1(h): 
    a = 0 # Límite inferior 
    b = 2 # Límite superior 
    n = int((b - a) / h) # Cantidad de intervalos 
    S = 0 # suma superior 
    s = 0 # suma inferior 
    for i in range(n): 
        xmin = a + i * h 
        xmax = a + (i + 1) * h 
        ymin = f(xmin) 
        ymax = f(xmax) 
        s = s + ymin * h 
        S = S + ymax * h 
    return(s, S) 

ej1(0.1) 


#%%
# Trapecios 

def ej2(h): #h va a ser el tamaño del intervalo 
    a = 0 #limite inferior
    b = 2 # limite superior
    n = int((b - a) / h) #cant de intervalos
    S = 0 # suma superior 
    for i in range(n): 
        xmin = a + i * h 
        xmax = a + (i + 1) * h 
        yizq = f(xmin) 
        yder = f(xmax) 
        S = S + (yizq + yder) / 2 * h # como el segmento superior del trapecio es lineal, es lo mismo calcular el punto medio como una altura media y hacer la fórmula del área del rectángulo con base h y altura (yizq + yder) / 2. 
    return(S) 

trapecios = ej2(0.1) 
trapecios



#%%
# Montecarlo 

# ATENCIÓN: Ojo que este script sólo tiene sentido para curvas encima del eje x. Para otras posibilidades, tenemos que reformular el script. 

def ej3(n): # la cant de puntos que voy a generar
    S = 0   # puntos que quedan debajo de la curva 
    ax = 0  # minimo valor de x en el cuadrilatero de integración. 
    bx = 2  # máximo valor de x en el cuadrilatero de integración. 
    ay = 0  # minimo valor de y en el cuadrilatero de integración. 
    by = 4  # máximo valor de y en el cuadrilatero de integración. 
    for i in range(n): #de 0 a n-1, los ciclos los determina el n q le puse
        x = np.random.uniform(ax, bx) #num aleatorios uniformemente distribuidos dentro del rango ax y bx
        y = np.random.uniform(ay, by) 
        if y <= f(x): # si y es menor que f(x) en cada ciclo
            S = S + 1 #a S le sumo 1 punto que cayo debajo de la curva
    return (S / n * (bx - ax) * (by - ay)) 

MonteCarlo = ej3(100) 
MonteCarlo


#%%
# Dibujito de Montecarlo 


import matplotlib.pyplot as plt #biblioteca de visualizacion
from scipy import linspace #crea un vector de numeros igualmente espaciados en un intervalo dado

 

def ej3_dibu(n): 
    S = 0   # puntos que quedan debajo de la curva
    ax = 0  # minimo valor de x en el cuadrilatero de integración.
    bx = 2  # máximo valor de x en el cuadrilatero de integración.
    ay = 0  # minimo valor de y en el cuadrilatero de integración.
    by = 4  # máximo valor de y en el cuadrilatero de integración. 
    x = linspace(ax, bx, 100) # cuantos más puntos ponga, más resolución tiene el gráfico 
    plt.plot(x, f(x), 'k') # traza la función f(x) en el intervalo de x definido por el renglon de arriba, utilizando una línea continua negra ('k').
    for i in range(n): 
        x = np.random.uniform(ax, bx) #Se genera un número aleatorio x entre ax y bx.
        y = np.random.uniform(ay, by) 
        plt.scatter(x, y, color = 'b') # ploteo el punto aleatorio de color azul 'b'
        if y <= f(x): 
            S = S + 1 #si el punto esta debajo o sobre la curva se aumenta el contador
    plt.show() #finalizado el for muestra todos los puntos y los graficos
    return(S / n * (bx - ax) * (by - ay)) #calculo de la aproximacion

MonteCarloDibu = ej3_dibu(100) #mientras mas puntos agregue mejor va a ser la aproximacion 
MonteCarloDibu



