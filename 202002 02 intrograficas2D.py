import numpy as np
import matplotlib.pyplot as plt
"""
--------------
parabola
--------------
Calcula la imagen de un numero real x por medio de la parabola y=x2-x-6
Recibe como parametro:
      un numero real "x" cualquiera
Retorna la imagen de x mediante la parábola y=x2-x-6
ejemplo:
     parabola(0) retorna -6
     parabola(-1) retorna -4
     parabola(1) retorna -6
"""
def parabola(x):
    y=x*x - x   -6
    return y
"""
--------------
f
--------------
Calcula la imagen de un numero real x por medio de la funcion y=4seno(x)
Recibe como parametro:
      un numero real "x" cualquiera que representa un angulo en radianes
Retorna la imagen de x mediante la funcion y=4seno(x), numero entre -4 y 4
ejemplo:
     f(0) retorna 0
     f(3.1416) retorna 0
     f(3.1416/2) retorna 4
"""
def f(x):
    y=4*np.sin(x)
    return y

"""
--------------
g
--------------
Calcula la imagen de un numero real x por medio de la funcion y=3coseno(x)
Recibe como parametro:
      un numero real "x" cualquiera que representa un angulo en radianes
Retorna la imagen de x mediante la funcion y=3coseno(x), numero entre -3 y 3
ejemplo:
     g(0) retorna 3
     g(3.1416) retorna -3
     g(3.1416/2) retorna 0
"""
def g(x):
    y=3*np.cos(x)
    return(y)

"""
--------------
recta
--------------
Calcula la imagen de un numero real x por medio de la funcion lineal y=0.7x +2
Recibe como parametro:
      un numero real "x" cualquiera que representa un punto del eje x
Retorna la imagen de x mediante la funcion y=0.7x +2
ejemplo:
     recta(0) retorna 2
     recta(1) retorna 2.7
     recta(-1) 1.3
"""
def recta(x):
    y=(0.7*x)  + 2
    return(y)


"""
--------------
graficarrecta
--------------
Grafica en una ventana (superficie de dibujo) la recta representa por la funcion recta
Recibe como parametro:
      un numero real "a" cualquiera que representa el limite inferior del intervalo de graficacion
      un numero real "b" mayor que "a" que representa el limite superior del intervalo de graficacion
      un numero entero positivo "numfig" que representa el identificador de la ventana de dibujo..
                si ya existe dibuja sobre la misma superficie, sino existe crea una nueva superficie
ejemplo:
     graficarrecta(0,100,1) retorna una grafica de la recta en el intervalo(0,100) 
     graficarrecta(-10,10,1) retorna una grafica de la recta en el intervalo(-10,10) 
"""
def graficarrecta(a,b,numfig):
    fig=plt.figure(numfig)
    plano=fig.gca()
    x=np.linspace(a,b,5)
    y=recta(x)
    plano.plot(x,y)
    return(fig)

"""
--------------
graficarrecta
--------------
Grafica en una ventana (superficie de dibujo) la parabola representa por la funcion parabola previamente desarrollada
Recibe como parametro:
      un numero real "a" cualquiera que representa el limite inferior del intervalo de graficacion
      un numero real "b" mayor que "a" que representa el limite superior del intervalo de graficacion
      un numero entero positivo "numfig" que representa el identificador de la ventana de dibujo..
                si ya existe dibuja sobre la misma superficie, sino existe crea una nueva superficie
ejemplo:
     graficarparabola(0,10,1) retorna una grafica de la parabola en el intervalo(0,10) 
     graficarrecta(-10,10,2) retorna una grafica de la parabola en el intervalo(-10,10) 
"""
def graficarparabola(a,b,numfig):
    fig=plt.figure(numfig)
    plano=fig.gca()
    x=np.linspace(a,b,100)
    y=parabola(x)
    plano.plot(x,y)
    return(fig)
 
"""
--------------
graficarfg
--------------
Grafica en una ventana (superficie de dibujo) las funciones f y g definidas previamente
Recibe como parametro:
      un numero real "a" cualquiera que representa el limite inferior del intervalo de graficacion
      un numero real "b" mayor que "a" que representa el limite superior del intervalo de graficacion
      un numero entero positivo "numfig" que representa el identificador de la ventana de dibujo..
                si ya existe dibuja sobre la misma superficie, sino existe crea una nueva superficie
ejemplo:
     graficarfg(0,10,1) retorna una grafica de las funciones f y g en el intervalo(0,10) 
     graficarfg(-10,10,2) retorna una grafica de la funciones f y g en el intervalo(-10,10) 
"""    
def graficarfg(a,b,numfig):
    fig=plt.figure(numfig)
    plano=fig.gca()
    x=np.linspace(a,b,100)
    y=f(x)
    w=g(x)
    plano.plot(x,y)
    plano.plot(x,w)
    return(fig)


fig=graficarparabola(-3,2,2)
fig=graficarfg(-6,6,fig.number+1)
fig=graficarrecta(-10,10,fig.number+1)
plt.show()
