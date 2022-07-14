#tupla ejercicio
def menu1():
 print("Bienvenido!,Consultar la temperatura de:")
 print("1.Bogota")
 print("2.Medellin")
 print("3.Cali")
 print("4.Inirida")
 print("5.Villavicencio")
 print("6.Cucuta")
 print("7.salir del programa")

def menu2():
 print("¿que deseas consultar?")
 print("1.Temperatura minima")
 print("2.Temperatura maxima")
 print("3.Temperatura promedio")
 print("4.salir del programa")

ciudades=("bogota",["-4°C","14°C","30°C"],"medellin",
          ["16°C","20°C","26°C"],"cali",["19°C","25°C","29°C"],
          "inirida",["23°C","25°C","30°C"],"villavicencio",["20","28°C","32"])

lista=list(ciudades)
lista.append("cucuta")
lista.append(["22°C","30°C","33°C"])

menu1()
print()
opc=int(input("Por favor,seleccione una ciudad : "))
print()
if opc ==1:
    menu2()
    print()
    opc1=int(input("selecciona una opcion: "))
    if opc1==1:
        print(min(lista[1]))
    elif opc1==2:
        print(max(lista[1]))
    elif opc1==3:
        print(lista[1][1])
    else:
        print("fin del programa")
elif opc ==2:
    menu2()
    print()
    opc1=int(input("selecciona una opcion: "))
    if opc1==1:
        print(min(lista[3]))
    elif opc1==2:
        print(max(lista[3]))
    elif opc1==3:
        print(lista[3][1])
elif opc ==3:
    menu2()
    print()
    opc1=int(input("selecciona una opcion: "))
    if opc1==1:
        print(min(lista[5]))
    elif opc1==2:
        print(max(lista[5]))
    elif opc1==3:
        print(lista[5][1])
elif opc ==4:
    menu2()
    print()
    opc1=int(input("selecciona una opcion: "))
    if opc1==1:
        print(min(lista[7]))
    elif opc1==2:
        print(max(lista[7]))
    elif opc1==3:
        print(lista[7][1])
elif opc ==5:
    menu2()
    print()
    opc1=int(input("selecciona una opcion: "))
    if opc1==1:
        print(min(lista[9]))
    elif opc1==2:
        print(max(lista[9]))
    elif opc1==3:
        print(lista[9][1])
elif opc ==6:
    menu2()
    print()
    opc1=int(input("selecciona una opcion: "))
    if opc1==1:
        print(min(lista[11]))
    elif opc1==2:
        print(max(lista[11]))
    elif opc1==3:
        print(lista[11][1])
else:
    print("fin del programa")



