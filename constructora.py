#una empresa constructora quiere averiguar sus gastos en materiales al año
#los tipos de materiales son
#1=cemento
#2=arena
#3=triturado
#4=herramientas
#se entregan los promedios mensuales en gastos de cada uno
#calcular=gastos anuales de cada tipo
#gastos del mes de enero  y diciembre
#gastos totales


#definir y declarar la funcion mostrar matriz
def mostrar_matriz(matriz):
    i=0
    for fila in matriz:
        i=i+1
        print("   ",i,"    ",fila)
#--------------------------------------------------------------------------------------------------------------------
#declaro la matriz con los datos columnas meses  filas tipo de material        
datos = [[282477, 316048, 312904, 114555, 140023, 335796, 308951, 189577, 108892, 296005, 120616, 302738],
[323079, 241725, 171165, 150321, 309985, 193723, 161784, 162379, 348065, 198975, 317126, 270337],
[220045, 333351, 199901, 271073, 278346, 293251, 197326, 119446, 267615, 344887, 234537, 298940],
[148509, 204424, 233324, 137845, 269708, 128168, 262617, 230523, 140836, 137738, 214435, 106948]]
print("")
#--------------------------------------------------------------------------------------------------------------------
#calculo el numero de filas 
filas= len(datos)
#calculo el numero de columnas
columnas =len(datos[0])
#---------------------------------------------------------------------------------------------------------------------
#sumatoria de la primera fila  por columnas - agregar columna con la sumatoria
for i in range (filas):
    sumaf = sum(datos[i])
    datos[i].append(sumaf)
#nueva matriz columna agregada
#---------------------------------------------------------------------------------------------------------------------
# la suma por columnas ,meses
mesessuma=[]
#recorer la matriz y agregar las sumatoria de las columnas
for j in range (13):
    sumac = sum([fila[j] for fila in datos ])
    mesessuma.append(sumac)
#------------------------------------------------------------------------------------------------------------------------
#PRUEBA
#imprimo el total recaudado en marzo y agosto
print ("                                                                MATERIALES DE CONSTRUCCION   ")
print (" ")
print (" ")
x=['Ene ','Feb ','Marz','Abril','May ','Jun   ','Jul   ','Agt  ','Sep ','Oct   ','Nov ',' Dic ',"total tipo"]
print("           ",x)
print (" ")
mostrar_matriz(datos)
print("=------------------------------------------------------------------------------------------------------")
#recaudo por mes
print("t.meses",mesessuma)
print("")
print (" ")
print("los gastos del mes de  enero fueron =",mesessuma[0])
print("los gastos del mes de  diciembre  fueron =",mesessuma[11])
#recaudo anual por tipo
print("#-----------------------gastos anuales -------------------")
print(" 1= cemento = ",datos[0][12])
print(" 2= arena =",datos[1][12])
print(" 3= triturado = ",datos[2][12])
print(" 4= herramientas  = ",datos[3][12])
#recaudo anual 
print("#------------------------------------------")
print("gasto anual  =",mesessuma[12])
print("#------------------------------------------")


