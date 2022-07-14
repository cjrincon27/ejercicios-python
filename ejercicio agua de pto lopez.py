
from  random import *   
def precio_barrio(a):
    return 2210*a
def descuento(a,b):                            
    return a-((a*b)/100)
def recargo_barrio(a,b):
    return (((a*50)/100)+b)*2210
def precio_vereda(a):
    return 2000*a
def recargo_vereda(a,b):
    return (((a * 30) / 100) + b) * 2000

print()
print("===============================================")

finalizar=0 
while finalizar!=2:
    print("Por favor, seleccione una opción")
    def opciones(a=print("1. Barrio \n2. Vereda")):
        return a + 0
    opc = opciones(int(input(":"))) 
    contar=0  
    if (opc  == 1): 
        n_familias=int(input("¿cuantas familias hay en el barrio?\n:"))
        for i in range (n_familias): 
            contar=contar+1
            print("--------------------------------------------")
            print("[ FAMILIA",contar,"]") 
            print("--------------------------------------------")
            nmes=0 
            for j in range (6): 
                nmes=nmes+1 
                print()
                print("MES",nmes,end=": ") 
                m3 = (randint(10, 25)) 
                print("Metros cubicos:",m3,end="  |  ") 
                print("Valor a pagar:","${:.0f}".format(precio_barrio(m3)),end="  |  ")
                if m3 <=15:    
                    print("Con descuento del 35%:","${:.0f}".format(descuento(precio_barrio(m3),35)))

                elif m3>=15 and m3<=20:
                    print("Con descuento del 15%:","${:.0f}".format(descuento(precio_barrio(m3),15)))

                elif m3>20:
                    print("Con recargo del 50%:","${:.0f}".format(recargo_barrio(m3,m3)))
            print()

    elif opc==2:      
        n_familias = int(input("¿cuantas familias hay en la vereda?\n:"))
        for i in range(n_familias):
            contar = contar + 1
            print("--------------------------------------------")
            print("[ FAMILIA", contar, "]")
            print("--------------------------------------------")
            nmes = 0
            for j in range(6):
                nmes = nmes + 1
                print()
                print("MES", nmes, end=": ")
                m3 = (randint(10, 25))
                print("Metros cubicos:", m3, end="  |  ")
                print("Valor a pagar:", "${:.0f}".format(precio_barrio(m3)), end="  |  ")
                if m3 <= 17:
                    print("Con descuento del 40%:", "${:.0f}".format(descuento(precio_barrio(m3), 40)))

                elif m3 >= 17 and m3 <= 22:
                    print("Con descuento del 20%:", "${:.0f}".format(descuento(precio_barrio(m3), 20)))

                elif m3 > 22:
                    print("Con recargo del 30%:", "${:.0f}".format(recargo_barrio(m3, m3)))
            print()
    else:
        print("OPCION INCORRECTA")
    print("==========================================================")
    finalizar=int(input("1. Seguiir registrando datos \n2. Terminar\n:")) 











