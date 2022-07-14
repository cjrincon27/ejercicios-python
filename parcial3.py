#definir y declarar la funcion mostrar matriz
def mostrar_matriz(matriz):
    for fila in matriz:
        print(fila)
#--------------------------------------------------------------------------------------------------------------------
#llenar matriz
#creo vector meses 
x=['Ene','Feb','Marz','Abril','Mayo','Junio','Julio','Agosto','Sept','Octu','Novi',' Dici']
print("",x)
print("")
from random import randint

def llenar_matriz(n):
    matriz = []

    for r in range(n):
        fila = []

        for c in range(12):
            fila.append(randint(100000, 350000))
        
        matriz.append(fila)
    
    return matriz

resultado = llenar_matriz(4)
mostrar_matriz(resultado)
print("")
#--------------------------------------------------------------------------------------------------------------------
#calculo del tamaño de la matriz
filas= len(resultado)
columnas =len(resultado[0])
print("El numero de filas es ..:",filas)
print("El numero de columnas es ..:",columnas)
print()
#---------------------------------------------------------------------------------------------------------------------
#sumatoria de la primera fila  por columnas - agregar columna con la sumatoria
for i in range (filas):
    sumaf = sum(resultado[i])
    resultado[i].append(sumaf)

 
print("suma por tipo (filas)")
#nueva matriz columna agregada
#recaudo por almacen en el semestre
mostrar_matriz(resultado)
print()
#------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------------------------------------------------------------------------
# agregar vector y almacenar los resulatdos por cada mes
nueva_fila=[]
#recorer la matriz y agregar las sumatoria de las columnas
for j in range (13):
    sumac = sum([fila[j] for fila in resultado ])
    nueva_fila.append(sumac)
#recaudo por mes
print("suma por  meses(columnas)")
print(nueva_fila)

#------------------------------------------------------------------------------------------------------------------------
#PRUEBA
#imprimo el total recaudado en marzo y agosto
print()
print("#------------------------------------------")
print("el total recaudado en",x[2],"es=",nueva_fila[2])
print("el total recaudado en",x[7],"es=",nueva_fila[7])
#imprimo resultado por tipo
print("#------------------------------------------")
print("total recaudado en motos ",resultado[0][12])
print("total recaudado en autos ",resultado[1][12])
print("total recaudado en camiones de 2 ejes  ",resultado[2][12])
print("total recaudado en camiones mas de dos ejes  ",resultado[3][12])
#imprimo total recaudado en el año
print("#------------------------------------------")
print("el total recaudado en el año es=",nueva_fila[12])
print("#------------------------------------------")


