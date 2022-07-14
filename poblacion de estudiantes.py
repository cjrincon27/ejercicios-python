import matplotlib.pyplot as plt
import numpy as np
import math

#=================================

def estudiantes():
    aux=90000
    for i in range (2010):
        #print(aux)
        #print("-----------")
        aux=aux-0.05*aux
        aux=round(aux)
        y.append(aux)


def años():
    for i in range(2010):
        aux=2002+i
        x.append(aux)

x=[]
y=[]
estudiantes()
años()

for i in range(9):
    print(x[i],y[i])

fig=plt.figure("Evolucion de la poblacion")
plt.plot(x,y)
plt.grid(True)
plt.show()