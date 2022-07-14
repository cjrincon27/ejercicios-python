import math  as mt
import numpy as np
import matplotlib.pyplot as plt

#serie de Fourier para calcular la descomposicion de una señal periodica en terminos de señales periodicas basicas

PI =mt.pi

#--------------------

#aN
#Autor: Lizeth Diaz, Luisa Muñoz, Camila Rangel
#Funcion que calcula el coeficiente de la serie de Fourier
#Parámetros:
    #n: numero entre -pi y pi con el cual se calculara el coeficiente 
#Retorno
    #: Retorna un valor entre -pi y pi
#Casos de prueba
    #An(2) --> 0
    #An(-2) --> 0
    #An(1) --> 0,6366197724


def aN(n):
    num = 1-(mt.pow(-1,n))
    den = (mt.pow(n,2))*PI
    return num / den

#print (aN(1))


#-----------------------------------

# bN (n) 
#Autor: Lizeth Diaz, Luisa Muñoz, Camila Rangel
#Funcion que calcula el coeficiente de la serie de Fourier
#Parámetros:
    #n: numero entre -pi y pi con el cual se calculara el coeficiente 
#Retorno
    #: Retorna un valor entre -pi y pi
#Casos de prueba
    #bN(1/2) --> 2
    #bN(2)    --> -0,5
    #bN(pi/2)  --> 0.6366197723675814

def bN(n):
    return (1/n)

#print (bN(PI/2))

#----------------------------------

#Sumatoria 
#Autor: Lizeth Diaz, Luisa Muñoz, Camila Rangel
#Funcion que halla la sumatoria de las funciones A0 y Bn producto coseno y seno respectivamente.
#Parametros
    #n: numero real de 1 a infinito
    #x: numero entre -pi y pi
#Retorno
    #: sumatoria
#Casos de prueba
    #sumatoria (1,2) --> 0.6443701224715508
    #sumatoria (2,2)  --> -0.7568024953079282
    #sumatoria (1,-2)  --> -1.1742247311798126

def sumatoria(n,x):
    i= 1
    suma=0    
    while (i<=n):
        an = aN(i)
        bn = bN(i)
        suma = suma + (an*np.cos(i*x)) + (bn*np.sin(i*x))
        i = i + 1
    return suma

#print (sumatoria(1,-2))

#--------------------
    
# a0()
#Autor: Lizeth Diaz, Luisa Muñoz, Camila Rangel
#Funcion que calcula el coeficiente de la serie de Fourier
#Retorno
    #a0: Retorna el valor del cociente


def a0():
    return (PI/2)

#print(a0())

#-------------------------------

#serieFourier
#Autor: Lizeth Diaz, Luisa Muñoz, Camila Rangel
#funcion que calcula la serie de Fourier que calcular la descomposicion de una señal periodica en terminos de señales periodicas basicas
#Parametros
    #n: numero real de 1 a infinito
    #x: numero entre -pi y pi
#Retorno
    #: La serie de Fourier
#casos de prueba:
    # serieFourier(2,-1) --> -0.12389926342823343
    # serieFourier(2, 2)  -->  0.028595668089520077
    # serieFourier(-3, 1)  -->   0.7853981633974483
    
def serieFourier(n,x):
    return (a0()/2) + sumatoria(n,x)


##
##    
##y=serieFourier(10,-PI)
##print(y)
##z=serieFourier(20,-3*PI/4)
##print(z)
##m=serieFourier(20,-PI/2)
##print(m)
##l=serieFourier(20,-PI/4)
##print(l)
##u=serieFourier(20,-0.05)
##print(u)
##t=serieFourier(20,0.05)
##print(t)
##v=serieFourier(20,PI/4)
##print(v)
##r=serieFourier(20,PI/2)
##print(r)
##o=serieFourier(20,PI)
##print(o)



#x=np.arange(-PI,PI,0.5)
#print(x)

#z=np.linspace(-PI,PI,5)
#print(z)

#y=serieFourier(20,z)
#print(y)
###################################################

#10.05.2022


##plt.plot(x,y,'b-')
##plt.grid(True)

def grafica(x,y):
    liferca= plt.figure()
    ax= liferca.gca()

    ax.plot(x,y,'b-',label='Serie Fourier')
    ax.grid(True)
    ax.legend(loc ="upper right")
    ax.set_title("Serie Fourier",color='red')
    ax.set_xlabel("x")
    ax.set_ylabel("f(x)")
    ax.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
    ax.set_xticklabels([r'$-\pi$', r'$-\pi/2$', "0", r'$+\pi/2$', r'$+\pi$'])
    ax.set_yticks([-1, 0, +1,+2,+3])
    ax.set_facecolor('k')
    
##    plt.plot(x,y,color='b-')
##    plt.grid(True)
##    plt.xlabel("valores entre -pi y pi")
##    plt.ylabel("valores entre -pi y pi")
    
    
x=np.linspace(-PI,PI,100)
y=serieFourier(200,x)

grafica(x,y)
plt.show()
