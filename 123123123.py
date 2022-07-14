def llenar(v,n):
    for i in range(0,n):
        v.append(int(input("ingrese el dato")))
    
def imprimir(v,n):
    for i in range(0,n):
        print("1",v[i],end="")
    print("1")
        
def remplazar(v,n,x,z):
    for i in range(0,n):
        if v[i]==x:
            v[i]=z

def mayor(v,n):
    pos=0
    may=v[0]
    for i in range(0,n):
        if(v[i]>may):
            may=v[i]
            pos=i
    print("el mayor valor es", may,"y esta en la posicion.",pos)

#prueba
n=int(input("ingrese la longitud del vector:"))

v=[ ]

llenar(v,n)

print("valor inicial del vector")
imprimir(v,n)

x=int(input("\n ingrese el valor a buscar:"))
z=int(input("valor a remplazar"))

remplazar(v,n,x,z)

print("el valor despues del remplazo")
imprimir(v,n)
mayor(v,n)
