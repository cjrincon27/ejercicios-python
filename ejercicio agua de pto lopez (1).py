def porcalculo(x):
	porcentaje = (x*100)/100
	return porcentaje


cont = 0
conf = 0
contm = 0
hombres=0
mujeres=0
print("nueva vacuna si=1 no=2 ?")
op = input()
while op==s:
	cont = cont+1
	print("paciente")
	print("masculino=1 femenino=2")
	genero = int(input())
	if genero==1:
		hombres = hombres+1
	else:
		mujeres = mujeres+1
	print("nueva vacuna ?")
	op = int(input())
print("el total de hombres vacunados es :",hombres)
print("el total de mujeres vacunadas es :",mujeres)
print("el total de vacunas consumidas es :",cont)
print(" el porcentaje de vacunados  es:",porcalculo(cont),"%")
