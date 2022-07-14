#en una cadena de supermercados se requiere hacer la contabilidad
#de sus ingresos anuales en tres de sus principales sedes 
#las ventas en los doce meses del año para cada uno de los 3 supermercados
#dado  en millones son

#20,40,35,13,45,57,23,45,57,87,24,78
#34,23,45,23,34,23,23,34,45,67,89,89
#23,34,12,34,4,3,32,56,34,56,67,78,34

#desarrollar un programa en lenguaje de programación Python donde se refleje el diseño de una matriz con los datos de cada sede  
#en el menú del programa se debe evidenciar
#1 )menor y mayor  valor en ventas del año en cada supermercado
#2)el total en millones de ventas al año en cada una de las sedes y el total general 
#3)el promedio de ventas en el año en cada sede y el promedio de la cadena 
#4) salir del menú

def f_menu():
 print("")
 print("")
 print("***************************************************************************")
 print("* * * * * MENU SUPERMERCADOS  * * * * *")
 print("1. menor y mayor mes de ventas ")
 print("2. totales en ventas ")
 print("3. promedio de ventas anuales por sede ")
 print("4. Salir")
 #recibe el vector calcula su maximo y minimo y retorna el vector 
def minmax (a):
            
             print("VENTAS ANUALES  ")
             print(" menor total  =",min(a))
             print(" mayor total =",max(a))
             return a 

   

#suma los valores de cada vector y retorna el total
def sumar (a):
 n=len(a)
 suma= 0
 i=0
 while i < n:
  suma=suma+a[i]
  i=i+1
 return suma
#calcula la suma de las posiciones de cada vector en los 3 vectores y retorna la
#suma de los 3 resultados


def f_totales(x,y,z):
 #usamos la funcion suma de vectores
 tsd1=sumar(x)
 tsd2=sumar(y)
 tsd3=sumar(z)

 print("=====================================================")
 print("TOTAL EN VENTAS POR SEDE ")
 print("sede 1:",tsd1)
 print("sede 2:",tsd2)
 print("sede 3:",tsd3)
 #sumamos para obtener el total de los supérmecados 
 ts=tsd1+tsd2+tsd3
 return ts


#calcula los promedios 
def f_prom(x,y,z):
#usamos la funcion suma de vectores y dividivmos en los meses del año
 Psd1=sumar(x)/12
 Psd2=sumar(y)/12
 Psd3=sumar(z)/12
 print("=====================================================")
 print("PROMEDIO POR SEDE  ")
 print("sede 1:",Psd1,"%")
 print("sede 2:",Psd2,"%")
 print("sede 3:",Psd3,"%")
 Ps=(Psd1+Psd2+Psd3)/3
 return Ps

#LOS DATOS ESTAN DADOS EN LA MATRIZ

datos =[[20,40,35,13,45,57,23,45,57,87,24,78],
         [34,23,45,23,34,23,23,34,45,67,89,89],
         [23,34,12,34,4,3,32,56,34,56,67,78,34]]

f_menu()
opc=0
while opc!= 4:
          
             opc=int(input("Digite Opcion..:"))
             if opc == 1:
                  print("=====================================================")
                  print(" sede1:",minmax(datos [0]))
                  print("")
                  print(" sede2:",minmax(datos [1]))
                  print("")
                  print(" sede3:",minmax(datos [2]))
                  print("")
             elif opc == 2:
                  print(" total en ventas en millones  :",f_totales(datos [0],datos [1],datos [2]))
             elif opc ==3:
                  print(" promedio en ventas de la cadena   :",f_prom(datos [0],datos [1],datos [2]),"%")
         
             f_menu()        
print("fin del programa")
