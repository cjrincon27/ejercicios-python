from random import*
#==================================================================
def portaxi(ctaxi,vserv):
    if ctaxi == 1:
        producido1=producido1+vserv
    if ctaxi == 1:
        producido2=producido2+vserv
    if ctaxi == 1:
        producido3=producido3+vserv
    return 
#--------------------------------------------------------------------
def sermas(tserv):
    if tserv == 1:
        serv1=serv1+1
    if tserv == 2:
        serv2=serv2+1
    if tserv == 3:
        serv3=serv3+1
x=serv1;        
if  serv1 < serv2 :
       x=serv2
if serv1< serv3:
       x=serv3
       
    return x
#--------------------------------------------------------------------
def mejorcliente(cedula,vserv):

    if vserv>servm:
      servm=vserv  
      mejor=cedula
    return 
#--------------------------------------------------------------------
i=0
n=int(input("ingrese el numero de carreras " ))
while i<n:
         i=i+1
         
         ctaxi = randint(1,3);
         cedula=randint(100000,500000);
         tserv = randint(1,3);
         vserv=randint(10000,50000);
         portaxi(ctaxi,vserv);
         masusado=sermas(tserv);
         mejorcliente(cedula,vserv);
print ("el mejor cliente es :",mejor)
print("el valor producido por el taxi1:"serv1)
print("el valor producido por el taxi1:"serv2)
print("el valor producido por el taxi1:"serv3)
print("el servicio mas usado es :",masusado)

         
         
         
    
