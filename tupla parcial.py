#tupla
caudal=( 50,75,46,22,80,65,8,25,65,19,23,23,34,45)
print(caudal)#muestro la tupla
print()
lista=list(caudal)#pasamos la tupla a lista
print("lista")
print(lista)#mostrar lista
print( )
print(" minimo=",min(lista),"maximo =",max(lista))
print( )
lista.extend([34,35,36])#agregar conjunto
print(lista)
lista.pop(16)#eliminar ultimo elemento
print()
print(lista)
lista[0]=100#modificar
print()
print(lista)



