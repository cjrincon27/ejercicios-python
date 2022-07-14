#declaramos la funcion multiplicacion de matrices rrecibe como parametro dos matrices
def m_matrices(m1,m2):
    if len(m1[0])==len(m2):#con el if comprobamos su dimension asi vemos si podemos multiplicar las matrices 
        m3=[]#declaramos la nueva matriz 
        for i in range (len(m1)):
            m3.append ([])
            for j in range (len(m2[0])):
                m3[i].append(0)
        for i in range (len(m1)):
            for j in range (len(m2[0])):
                for k in range (len(m1[0])):
                    m3[i][j] += m1[i][k]*m2[k][j] #recorremos las matrices y vamos multiplicando 
        return m3 #retornamos la nueva matriz obtenida 
    else:
        return None  #si no se cumple la condicion del if retornamos none 

#casos de prueba 

a=[[87,92,95],
   [90,94,96]] 

b=[[225000,235000],
   [195000,215000],
   [186000,202500]]
#llamamos la funcion multiplicacion y almacenamos la matriz que retorna en la variable c
c = m_matrices(a,b)
#imrpimimos las matrices a y b 
print (a)
print()
print (b)
print()
# evaluamos lo que nos retorna la fucion 
if c==None:
    print ("no se puede multiplicar")
else:#imprimimos la matriz c de forma ordenada 
    for fila in c:
        print ("[",end="")
        for elemento in fila:
            print (elemento,end="|")
        print ("]")
print()
#calculamos el total imprimiendo la suma de las filas de la matiz c
print ("total de las ventas primer consecionario =",c[0][0] +  c[0][1])
print ("total de las ventassegundo consecionario =",c[1][0] +  c[1][1])

