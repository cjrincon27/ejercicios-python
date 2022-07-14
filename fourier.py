# Número pi 3.141592653589793, primeros 15 decimales
pi = 3.141592653589793
# Se establencen los coecificentes de la función
a0 = (pi/2)
w0 = 1

# factorial(n)
# Autor: Augusto Brugés Romero
# Función que calcula el factorial de un número, sabiendo que el factorial de cero(0) es uno (1)
# Parámetros:
# n: Número entero positivo al que se le va a calcular el factorial
# Retorno
# Numero entero positivo con el calculo del factorial
# Casos de prueba
# factorial(0) --> 1
# factorial(5) --> 120


def factorial(n):
    rtaFactorial = 1
    if(n > 0):
        i = 1
        while (i <= n):
            rtaFactorial = rtaFactorial * i
            i = i + 1
    return rtaFactorial

#potencia(pBase, pExpo)
# Autor: Augusto Brugés Romero
# Función que calcula la potencia de un numero dado su base y su exponente
# Parámetros:
    # pBase: Número entero positivo que corresponde a la base
    # pExpo: Número entero positivo que corresponde al exponente
# Retorno:
    # rtaPot: Número entero positivo que corresponde al cálculo de la potencia
# Caso de prueba
    # potencia(2,5)--> 32
    # potencia(2,0)--> 1
    # potencia(0,2)--> 0


def potencia(pBase, pExpo):
    rtaPot = 1
    if(pExpo >= 0):
        i = 0
        while(i < pExpo):
            rtaPot = rtaPot * pBase
            i = i+1
    return rtaPot

# gradeToRadi(angule)
# Autor: Augusto Brugés Romero
# Función que convierte un ángulo dado en grados a radianes
# Parámetros
    # angule:  Numero real positivo, que representa el ángulo en grados
# Retorno
    # rtaRadianes: Número real positivo que representa el ángulo en radianes


def gradeToRadi(angule):
    rtaRadianes = 3.14159 * angule / 180
    return rtaRadianes


# sumaSeno()
def sumaSeno(gradeRadianes, n):
    rta = 0
    if (n > 0):
        k = 0
        while (k <= n):
            rta = rta + (potencia(-1, k) * potencia(gradeRadianes,
                                                    (2*k+1)) / factorial(2*k + 1))
            k = k+1
    return rta

#NOTA: La función calcularSeno fue modificada eliminando la conversión de grados a radianes
# calcularSeno()
# Autor: Augusto Brugés Romero
# Función que calcula el seno de un angulo dado en grados utilizando la seria de Tylor.  n es el número de puntos usados para el cálculo
# Parámetros
    # grade:  Valor del angulo en grados
    # n: Numero entero positivo que determina el numero de sumas a realizar para el cálculo
# Return:
    # senoAngulo:  Valor del seno del ángulo dado
# casos de prueba
    # calcularSeno(0)       -->  0
    # calcularSeno(pi/2)    -->  1
    # calcularSeno(pi)      -->  0
    # calcularSeno(3pi/2)   --> -1
    # calcularSeno(2pi)     -->  0
def calcularSeno(angle, n):
    #angleRad = gradeToRadi(angle)
    seno = sumaSeno(angle, n)
    return seno


# sumaCoseno()
def sumaCoseno(gradeRadianes, n):
    rta = 0
    if (n > 0):
        k = 0
        while (k <= n):
            rta = rta + (potencia(-1, k) *
                         potencia(gradeRadianes, (2*k)) / factorial(2*k))
            k = k+1
    return rta


#NOTA: La función CalcularCoseno fue modificada eliminando la conversión de grados a radianes
# Autor: Augusto Brugés Romero
# Función que calcula el Coseno de un angulo dado en radianes utilizando la seria de Tylor.  n es el número de puntos usados para el cálculo
# Parámetros
    # grade:  Valor del angulo en radianes
    # n: Numero entero positivo que determina el numero de sumas a realizar para el cálculo
# Return:
    # senoAngulo:  Valor del Coseno del ángulo dado
# casos de prueba
    # CalcularCoseno(0)     --> 1
    # CalcularCoseno(pi/2)  --> 0
    # CalcularCoseno(pi)    --> -1
    # CalcularCoseno(3pi/2) --> 0
    # CalcularCoseno(2pi)   --> 1
def calcularCoseno(angle, n):
    #angleRad = gradeToRadi(angle)
    coseno = sumaCoseno(angle, n)
    return coseno


# sumaFourier(x, precision)
# Autor: Juan sebastian galva, Natali jaimes
# Función que calcula las n sumas parciales para de la serie de Fourier con los coeficientes
# a0=pi/2, an=(1-(-1)^n)/(n^2*pi), bn=1/n
# Parámetros:
    # x: Número real para el cuál se calculará las sumas parciales, entre -pi y pi
    # precision: Número de sumas parciales de la serie a realizar
# Retorno
    # Numero real con el cálculo de las n sumás parciales
# Casos de prueba
# Tomando pi igual a 3.141592653589793
    # suma(pi)       --> 0
    # suma(pi/2)     --> pi/2 ~ 1.5707963267948966
    # suma(-pi/2)    --> 0

def sumaFourier(x, precision):
    suma = a0/2
    n = 1
    while(n <= precision):
        an = (1-potencia((-1), n))/(potencia(n, 2)*pi)
        bn = 1/n
        sumaparc = (an*calcularCoseno((n*w0*x), 50)) + (bn*calcularSeno((n*w0*x), 50))
        suma = suma + sumaparc
        n = n + 1
    return suma

    

# f(x, n)
# Autor:Juan sebastian galvan, Natali Jaimes
# Función que calcula la aproximación de f(x) para un x dado, a partir de n sumas parciales
# Parámetros:
    # x: Número real para el cuál se calculará f(x), entre -pi y pi
    # n: Número de sumas parciales de la serie a realizar
# Retorno
    # Numero real con el cálculo de f(x)
# Casos de prueba
# Tomando pi igual a 3.141592653589793
    # f(pi)       --> 0
    # f(pi/2)     --> pi/2 ~ 1.5707963267948966
    # f(-pi/2)    --> 0
def f(x, n):
    if(n>0):
        print(sumaFourier(x, n))
    else:
        print('Ingrese un valor válido (mayor que 0)')


# Casos de prueba
print('Casos de prueba f(x), suma(x)')
f(pi,10)
f(pi/2,10)
f(-pi/2,10)
f(0.257448334,10)
