#la universidad de pamplona a contarado los servicios de una empresa contruztura para hacer reparaciones en
#todas sus intalaciones .la universidad comparte con la empresa el total de metros cuadrados de cada espacio a remodelar
#cada metro cuadrado de remodelacion tiene un costo de 20.000$.
#la universidad requiere conocer :
#1)el costro toal de reparaciones
#2)el mayor numero de metros cuadrados y el menor numero
#3)un promedio de metros cuadrados de reparacion
#4)las medidas mayores al promedio y caclular su costo 



#primero importamos la libreria numpy
import numpy as np
#declaramos nuestro vector con los datos 
dim=np.array([ 23 , 31, 40 , 15 , 10 , 16 , 30 , 19 , 12,23 , 31, 40 , 15 , 10 , 16 , 30 , 19 , 12,23 , 31, 40 , 15 , 10 , 16 , 30 , 19 ,
              12,23 , 31, 40 , 15 , 10 , 16 , 30 , 19 , 12,23 , 31, 40 , 15 ,23 , 31, 40 , 15 , 10 , 16 , 30 , 19 , 12,
              23 , 31, 40 , 15 , 10 , 16 , 30 , 19 , 12,23 , 31, 40 , 15 , 10 , 16 , 30 , 19 , 12,23 , 31, 40 , 15 , 10 , 16 , 30 , 19 ,
              12,23 , 31, 40 , 15 , 10 , 16 , 30 , 19 , 12,23 , 31, 40 , 15 , 10 , 16 , 30 , 19 , 12,
              23 , 31, 40 , 15 , 10 , 16 , 30 , 19 , 12,23 , 31, 40 , 15 , 10 , 16 , 30 , 19 , 12,23 , 31, 40 , 15 , 10 , 16 , 30 ,
              19 , 12,23 , 31, 40 , 15 , 10 , 16 , 30 , 19 , 12,23 , 31, 40 , 15 , 10 , 16 , 30 , 19 , 12,
              10 , 16 , 30 , 19 , 12,23 , 31, 40 , 15 , 10 , 16 , 30 , 19 , 12,23 , 31, 40 , 15 , 10 , 16 , 30 , 19 , 12, 20, 35 ,
              32 , 23 , 31, 40 , 15 , 10 , 16 , 30 , 19 , 12 ])

#prueba
print("REPARACIONES UNIVERSIDAD DE PAMPLONA ")
print("",)
print("",dim)
print("",)
costo=np.sum(dim)*20000
promedio=np.sum(dim)/(dim.size)
print("costro total de reparaciones =",costo)
print('mayor medida  =',np.amax(dim))
print('menor medida = ',np.amin(dim))
print("promedio de metros cuadrados ",promedio)
print("")
print("")
print("las medidas en metros mayores al promedio son :",)
print("",)
a=(dim[(dim >promedio)])
print("",a)
print("",)
print("  el costo de repacion de las medidas mayores al promedio es  = :",np.sum(a)*20000)



