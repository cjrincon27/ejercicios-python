#este programa calcula la nota definitiva de programacion 1

def fnexamen (a,b,c):
    a: float; b: float; c: float
    not1=(a*0.60)
    print ("la nota del examen es ", a)
    not2=(b*0.25)
    print ("la nota de los quices es ", b)
    not3=(c*0.15)
    print ("la nota de los trabajos es ", c)
    d=(not1+not2+not3)
    return d




n1=float(input("ingrese el valor del examen:  "))
n2=float(input("ingrese el valor de los quices:  "))
n3=float(input("ingrese el valor de los trabajos:  "))
print ("======================")

definitiva = fnexamen (n1,n2,n3)
print ("======================")
if definitiva >3.0 :
    
         print ("el estudiante aprobo", definitiva)
else:
         print("el estudiante reprobo", definitiva)
