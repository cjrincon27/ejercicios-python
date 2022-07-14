#importamos la libreria ramdom
import random
#definimos la funcion promedio recibe como parametro el vector (a) 
def promedio (a):
    n=len(a) #contamos las pocisiones del vector 
    suma= 0
    i=0
    while i < n:
        suma=suma+a[i] #sumamos las posiciones  
        i=i+1
    print("total de habitantes =",suma)   #imprimimos el total   
    prom=suma/n #calculamos el promedio  
    return prom #retorna el promedio
#definimos la funcion que llena el vector de forma aletorea  recibe como parametro el numero de ciudades 
def vector (n):
             a=[]#declaramos vector
             #utilizamos el for para ir llenando el vcetor de forma aletorea con la funcion random
             for i in range (n):
                          a.append(random.randint(1000000,1000000000))
             return a # retornamos el vector 

 #casos de prueba
nciudades=10
print(" habitantes por ciudad  :",vector(nciudades))
print(" promedio de habitantes  :",promedio(vector(nciudades)))

