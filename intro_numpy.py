import numpy as np

#Autor:Augusto Brugés Romero
#Funcion que permite crerar una matriz m x n de ceros
#Parámetros:
    #nFilas : Valor entero con el numero de filas de la matriz
    #nColumnas : Valor entero con el numero de coumnas de la matriz
#retorna
    #matriz: Objeto ndarray, con sus elementos en cero con shape nFilas nColumnas
def matrizZeros(nFilas, nColumnas, tipo):
    matriz = np.zeros( (nFilas,nColumnas), dtype = tipo )
    return matriz

#Autor:Augusto Brugés Romero
#Funcion que permite crerar una matriz m x n de ceros
#Parámetros:
    #nFilas : Valor entero con el numero de filas de la matriz
    #nColumnas : Valor entero con el numero de coumnas de la matriz
#retorna
    #matriz: Objeto ndarray, con sus elementos en cero con shape nFilas nColumnas
def matrizOnes(nFilas, nColumnas, tipo):
    matriz = np.ones( (nFilas,nColumnas), dtype = tipo )
    return matriz

#Autor:Augusto Brugés Romero
#Funcion que permite crerar una matriz m x n de un valor determinado
#Parámetros:
    #nFilas : Valor entero con el numero de filas de la matriz
    #nColumnas : Valor entero con el numero de coumnas de la matriz
    #valueIni : Valor que corresponde al valor inicial de todos los elementos de la matriz
#retorna
    #matriz: Objeto ndarray, con sus elementos en cero con shape nFilas nColumnas
def matrizValues(nFilas, nColumnas, valueIni, tipo):
    matriz = np.full( (nFilas, nColumnas),5,dtype = tipo)
    return matriz


def matrizIdentidad(nFilas, nColumnas, tipo):
    matriz = np.eye( nFilas, nColumnas,dtype = tipo)
    return matriz

#Autor:Augusto Brugés Romero
#Funcion que permite crerar una matriz m x n con valores enteros aleatorios
#Parámetros:
    #nFilas : Valor entero con el numero de filas de la matriz
    #nColumnas : Valor entero con el numero de coumnas de la matriz
    #valueIni : Valor inicial de los valores aleatorios
    #valueFin : Valor inicial de los valores aleatorios
#retorna
    #matriz: Objeto ndarray, con sus elementos en cero con shape nFilas nColumnas
def matrizAleatorioEntero(nFilas, nColumnas, valueIni, valueFin):
    matriz = np.random.randint(valueIni,valueFin, (nFilas,nColumnas) )
    return matriz

mat_prueba = matrizAleatorioEntero(2,3,1,20)
print(mat_prueba)

    
