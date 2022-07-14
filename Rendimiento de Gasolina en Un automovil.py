import matplotlib.pyplot as plt
import numpy as np
import math
import sys
clear = lambda:os.system('cls')
#==================================================================
def galones(cantidadenprecio, preciogalon):
    gal = 1
    gal = (gal * cantidadenprecio) / preciogalon
    return gal
#--------------------------------------------------------------------
def litros(cantidadenprecio, preciogalon):
    gal = 1
    lit = (galit * (gal * cantidadenprecio) / preciogalon)
    return lit
#--------------------------------------------------------------------
def consumogasolina(cantidadenprecio, preciogalon, km):
    gal = 1
    lk = ((km * (galit * (gal * cantidadenprecio) / preciogalon)) / Tanqgl) / (
            galit * (gal * cantidadenprecio) / preciogalon)
    return lk
#--------------------------------------------------------------------
def gasolinarestante(cantidadenprecio, preciogalon, km):
    gal = 1
    rest = ((galit * (gal * cantidadenprecio) / preciogalon)) - (
            ((km * (galit * (gal * cantidadenprecio) / preciogalon)) / Tanqgl) / (
            galit * (gal * cantidadenprecio) / preciogalon))
    return rest
#--------------------------------------------------------------------
def kilomestrosrestantes(cantidadenprecio, preciogalon, km):
    gal = 1
    kmr = ((galit * (gal * cantidadenprecio) / preciogalon) - (
            ((km * (galit * (gal * cantidadenprecio) / preciogalon)) / Tanqgl) / (
            galit * (gal * cantidadenprecio) / preciogalon))) * Tanqgl
    return kmr
#--------------------------------------------------------------------
galit=3.78541
Tanqgl=12
preciogalon = int(input(" \nEscriba el precio de la gasolina por Galon: "))
aux = 1
aux2 = 0
mat = []
x=[]
y=[]
y2 = []
while aux == 1:
    vec = []
    print("\n\t\tAuto Numero ",aux2+1)
    aux2 = aux2 +1
    cantidadenprecio = int(input(" Ingrese el precio pagado por la gasolina: "))

    vec.append(cantidadenprecio)

    print(" La Cantidad En Galones Es: ", galones(cantidadenprecio, preciogalon))

    aux3 = galones(cantidadenprecio, preciogalon)
    vec.append(aux3)

    print(" La cantidad en Litros es de: ", litros(cantidadenprecio, preciogalon))

    aux3 = litros(cantidadenprecio, preciogalon)
    vec.append(aux3)

    print(" \n¿Ha conducido alguna distancia desde que le suministro la gasolina al automovil? escriba  SI O NO: ")
    op  = input()
    if  op == " no ":
        print("Saliendo...")
    else:
        km = int(input(" Ingrese la Cantdad de Kilometros recorridos: "))

        vec.append(km)

        print(" Los Litros de gasolina consumidos en la distancia recorrida es: ",
                consumogasolina(cantidadenprecio, preciogalon, km))

        aux3 = consumogasolina(cantidadenprecio, preciogalon, km)
        vec.append(aux3)

        print(" La gasolina Restante Es De: ", gasolinarestante(cantidadenprecio, preciogalon, km), "L.")
        print(" Alcanza Para otros: ", kilomestrosrestantes(cantidadenprecio, preciogalon, km), " km.")
    mat.append(vec)
    aux = int(input(" \npresione 1 para registrar otro vahiculo o 0 para salir: "))

print("\nEstadisticas De ",aux2," Autos Que Se Ingresaron")
#--------------------------------------------------------------------
for i in range(aux2):
    print("\n\t\t| Auto #", i + 1, "|\n")

    print("|       Tanqueo         |=","|", mat[i][0],"Pesos|")

    print("|  Cantidad En Litros   |=","|", mat[i][2]," L.|")

    print("| Kilometros Recorridos |=","|", mat[i][3], " Km.|")

    print("| Combustible Consumido |=","|", mat[i][4], " L.|")

print(" \nHasta Luego. \n")

#==========================================================================
for i in range(aux2):
    x.append(i)

for i in range(aux2):
    #print(mat[i][3])
    print("\n\t\t| Auto #", i + 1, "|\n")
    aux = (mat[i][3])
    y2.append(aux)
    aux = i
    auxo = (mat[i][4])
    y.append(auxo)
    print(x)

    print(y)
    print(y2)


fig=plt.figure("Evolucion de la poblacion")
plt.plot(x,y2,y)
plt.grid(True)
plt.show()