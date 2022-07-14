#Ejercicio: En una fábrica se quiere tener registrado las compras mensuales  realizadas a los proveedores de los materiales:
# 	1kg Acero = 10.000$ 
# 	1kg Aluminio= 15.000 $
# 	1kg Polietileno=20.000$
# Los cuales se asumen comprados por Kg. Realizar un programa que le permita al operador .
#kilogramos por material comprados al año y total de material anual
 #costo anual  por material comprado  
# costo total en compras anual


def f_menu():
    print("* * * * * MENU DE OPCIONES * * * * *")
    print("1.  kilogramos por material comprados al año")
    print("2. costo anual  por material comprado  ")
    print("3. costo total en compras anual")
    print("4. Salir")
#suma los valores de cada vector retorna el total     

def sumar (a):
    n=len(a)
    suma= 0
    i=0
    while i < n:
        suma=suma+a[i]
        i=i+1
    return suma
#calcula la msuma de las posiciones de cadavector en los 3 vectores retorna la suma de los 3 resultados 


def f_kilogramos(x,y,z):
    kac=sumar(x)
    kal=sumar(y)
    kpl=sumar(z)
    print("=====================================================")
    print("TOTAL DE KILOGRAMOS ANUALES POR MATERIAL ")
    print("acero:",kac)
    print("Aluminio:",kal)
    print("Polietileno:",kpl)
    kt=kac+kal+kpl
    return kt
#calcula el costo segun la suma de cada vector retorna el total 
def f_costo(x,y,z):
    kac=sumar(x)*10000
    kal=sumar(y)*15000
    kpl=sumar(z)*20000
    print("=====================================================")
    print("COSTO ANUAL POR MATERIAL ")
    print("acero:",kac)
    print("Aluminio:",kal)
    print("Polietileno:",kpl)
    ct=kac+kal+kpl
    return ct


ac=[14,12,34,56,2,34,56,78,46,24,12,23]
al=[12,44,76,88,20,76,87,34,34,45,45,56]
p=[12,56,34,76,87,98,57,67,23,24,23,24]

f_menu()

opc=int(input("Digite Opcion..:"))
if opc == 1:
     print(" total de kilos de material anual :",f_kilogramos(ac,al,p))
elif opc == 2:
    f_costo(ac,al,p)
elif opc ==3:
    print(" el costo total en compra de materiales anual es  :",f_costo(ac,al,p))
else:
    print("fin del programa")
