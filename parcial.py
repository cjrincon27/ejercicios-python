def aporte(a):
	if a<=17:
		op = 5000
	else:
		if a>=18 and a<=20:
			op = 7000
		else:
			op = 10000
	return op

def actividad(a,b):
	if a==1:
		if b<=19:
			x = 1
		else:
			x = 2
	else:
		if b<=20:
			x = 3
		else:
			x = 4
	return x

if __name__ == '__main__':
	print("ingrese genero 1 femenino , 2 masculino ")
	s = input()
	print("ingrese edad ")
	e = input()
	print("el aporte a realizar es de ",aporte(e))
	acti = actividad(s,e)
	if acti==1:
		print(" envío de invitaciones a participantes")
	elif acti==2:
		print("  Gestión de ingreso de participantes al evento ")
	elif acti==3:
		print("Organización de silletería")
	elif acti==4:
		print(" Acomodación de participantes")
	

