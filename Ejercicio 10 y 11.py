import numpy as np
from matplotlib import pyplot as plt

def funcion(x):
    return -np.power(x, 3)-np.cos(x)

def funcion2(x):
    return -3*np.power(x, 2)+np.sin(x)*1

def newton(xi, maxiteraciones, cota):
    error = 1
    i = 1
    print("i | xi | fxi |fdxi | xr | error")
    while error > cota:
        xr = xi - (funcion(xi)/funcion2(xi))
        error = np.abs((xr-xi)/xr)
        xi = xr
        i += 1
        print("Raiz:", xr, " Error:", error)

newton(-1, 10, 0.001)

vectorx = np.arange(-4, 4, 0.01)

plt.plot(vectorx, funcion(vectorx))
plt.grid("x")
plt.grid("y")
plt.show()