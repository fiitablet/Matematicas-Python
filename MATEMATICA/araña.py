import matplotlib.pyplot as plt
from scipy import cos, linspace

def cobweb(f, x0, N, a = 0, b = 1):
    # plot the function being iterated
    t = linspace(a, b, N)
    plt.plot(t, f(t), 'k')
    # plot the dotted line y = x
    plt.plot(t, t, "k:")
    # plot the iterates
    x, y = x0, f(x0)
    for _ in range(N):
        fy = f(y)        
        plt.plot([x, y], [y,  y], 'b', linewidth = 1)
        plt.plot([y, y], [y, fy], 'b', linewidth = 1)
        x, y = y, fy
    plt.show()

cobweb(cos, 1, 20) 
cobweb(lambda x: x**2, 0.6, 20) # lambda define una función anónima 
cobweb(lambda x: 4.0 * x * (1 - x), 0.1, 100) 



