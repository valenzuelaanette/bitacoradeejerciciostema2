import numpy as np
import matplotlib.pyplot as plt


def f(x):
    return 2*np.sin(np.pi*x)+x

#MÉTODO DE LA SECANTE

def secante(xinf, xsup, cota, maxiteraciones):
    error = 1
    i = 1
    while error > cota:
        #NUEVA APROXIMACIÓN (RAÍZ)
        xr = xinf - ((f(xinf)*(xinf-xsup))/(f(xinf)-f(xsup)))
        
        #CALCULANDO EL ERROR
        error = np.abs((xr-xinf)/xr)
        print("Iteración:", i, " xsup:", xsup, "xinf:",
              xinf, " Raiz:", xr, " Error:", error)
        
        #REASIGNANDO VALORES
        xinf = xsup
        xsup = xr
        i += 1
        
        #IMPRIMIENDO EL RESULTADO DE LA RAÍZ Y EL ERROR
        if(error <= 0.01):
            print("La raíz es: ", xr, " f(raíz): ", f(xr))
            print("Con un error de: ", error)
            plt.plot(xinf, 0, 'o', color="g")
            plt.plot(xsup, f(xsup), 'o', color="y")


#LLAMANDO AL MÉTODO DE LA SECANTE
secante(1.5, 2, 0.01, 10)

#REALIZANDO LA GRÁFICA
x = np.linspace(1, 2, 7)
plt.plot(x, f(x))
plt.title("Ejercicio 8")
plt.grid('on')
plt.show()