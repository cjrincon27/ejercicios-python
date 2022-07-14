#definir y declarar la funcion mostrar matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)

 

#definir matriz
matriz = [
              [25,68,34,65,43,68],
              [22,88,34,62,34,12],
              [89,76,43,55,33,66],
              [54,33,11,55,66,77],
              [83,41,65,77,23,21],
              ]
#llamar la funcion
mostrar_matriz(matriz)
#--------------------------------------------------------------------------------------------------------------------
#calculo del tamaño de la matriz
filas= len(matriz)
columnas =len(matriz[0])
print("El numero de filas es ..:",filas)
print("El numero de columnas es ..:",columnas)
print()
#---------------------------------------------------------------------------------------------------------------------
#sumatoria de la primera fila  por columnas - agregar columna con la sumatoria
for i in range (filas):
    sumaf = sum(matriz[i])
    matriz[i].append(sumaf)

 

#nueva matriz columna agregada
#recaudo por almacen en el semestre
mostrar_matriz(matriz)
print()
#------------------------------------------------------------------------------------------------------------------------
# agregar vector y almacenar los resulatdos por cada mes
nueva_fila=[]

 

#recorer la matriz y agregar las sumatoria de las columnas
for j in range (columnas):
    sumac = sum([fila[j] for fila in matriz ])
    nueva_fila.append(sumac)
#recaudo por mes
print(nueva_fila)
#------------------------------------------------------------------------------------------------------------------------
print()
#recaudo semestral
nueva_fila.append (sum(nueva_fila))
print(nueva_fila)
