def sumar (v):
    n=len(v)
    suma= 0
    i=0
    while i < n:
        suma=suma+v[i]
        i=i+1
    return suma
v=[12,44,76,88,20,76,87]
print (" elementos del vector",v)
s=sumar(v)
print ("suma de los vectores",s)
print (v[2])
print (v[6])
