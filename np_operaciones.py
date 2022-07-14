import numpy as np

def concatenar(arr1,arr2):
    arr = np.concatenate((arr1,arr2), axis=1);
    return arr

def dividir(arr, numero):
    arr = np.array_split(arr,numero);
    return arr

def buscar(arr, valor):
    lista = np.where(arr % valor == 0)
    return lista


def sumar(arr1,arr2):
    arr = np.subtract(arr1, arr2)
    return arr


        
#Codigo de prueba
lista_1 = np.array([[1,2],[3,4]])
lista_2 = np.array([[4,5],[6,7]])

print(sumar(lista_1, lista_2))






