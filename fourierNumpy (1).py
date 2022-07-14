import math as mt

import numpy as np
import matplotlib.pyplot as plt


PI = mt.pi



#Función que permite obtener los coeficientes An asociados a la funcion coseno de la serie.
#Autor: Augusto Brugés
#Parámetros
	#n: Numero entero positivo, que corresponde al número de iteración de la sumatoria
#Retorno
	#a_n: Valor correpondiente al calculo del coeficiente
#casos de prueba
    #obtenerAn(1) = 2/PI
    #obtenerAn(2) = 0
    #obtenerAn(3) = 2/9*PI
def obtenerAn(n):
    a_n = 0
    a_n = (1 - mt.pow(-1,n)) / (n*n*PI) 
    return a_n


#Función que permite obtener los coefincientes Bn asociados a la funcion coseno de la serie.
#Autor: Augusto Brugés
#Parámetros
	#n: Numero entero positivo, que corresponde al número de iteración de la sumatoria
#Retorno
	#b_n: Valor correpondiente al calculo del coeficiente
#casos de prueba
    #obtenerBn(1) = 1
    #obtenerBn(2) = 0.5
    #obtenerBn(3) = 0.3333
def obtenerBn(n):
    b_n = 0
    b_n = 1 / n
    return b_n


#Función que permite acumular los terminos de la serie de fourier, elementos que corresponden a sumatorias de funciones sinusoidales
#Autor: Augusto Brugés Romero
#Parametros
	#x: Valor del grado en radianes
	#limite: Numero de elementos de la serie.  Es un valor entero positivo
#Retorno:
	#sumaParcial:  Valor de la suma de cada uno de los elementos de la serie.  
#Casos de prueba
def obtenerSumatoriaParcial(x,limite):
    
    sumaParcial = 0
    n = 1;    
    while (n <= limite):

        a_n = obtenerAn(n)
        b_n = obtenerBn(n)        

        #sin = mt.sin(n*x)
        #cos = mt.cos(n*x)

        sin = np.sin(n*x)
        cos = np.cos(n*x)

        #print("an = {} , b_n = {}, sin = {}, cos = {}".format(a_n,b_n,sin,cos))        
        
        sumaParcial = sumaParcial + (a_n*cos + b_n*sin)
        
        n = n+1
    return sumaParcial


def calcularSerieFourier(x):
    rta = 0
    a_0 = PI / 2
    rta = a_0/2 + obtenerSumatoriaParcial(x,20)
    return rta


print("-PI = {} , serie = {} ".format(-PI,calcularSerieFourier(-PI)))
print("-3*PI/4 = {} , serie = {} ".format(-2*PI/3,calcularSerieFourier(-3*PI/4)))
print("-PI/2 = {} , serie = {} ".format(-PI/2,calcularSerieFourier(-PI/2)))
print("-PI/4 = {} , serie = {} ".format(-2*PI/3,calcularSerieFourier(-PI/4)))
print("0 = {} , serie = {} ".format("0",calcularSerieFourier(0.1)))
print("PI/4 = {} , serie = {} ".format(-2*PI/3,calcularSerieFourier(PI/4)))
print("PI/2 = {} , serie = {} ".format(-PI/2,calcularSerieFourier(PI/2)))
print("3*PI/4 = {} , serie = {} ".format(-2*PI/3,calcularSerieFourier(3*PI/4)))
print("PI = {} , serie = {} ".format(-PI,calcularSerieFourier(PI)))




x = np.arange(-PI,PI,0.5) #Obtenemos el rango de grafica
y = calcularSerieFourier(x)#

print(x)
print(y)

#plt.plot(x,y)
#plt.show()
