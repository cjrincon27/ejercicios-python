def estresm2(x, z):
	e = x/(z*0.3)
	return e

def estresm1(x):
	e = x/10
	return e

def estres25(x, z):
	e = (z*x)/100
	return e

def estres15(x, z):
	e = x/z
	return e

if __name__ == '__main__':
	print("ingrese el sexo ")
	print("1=hombre")
	print("2 = mujer")
	s = int(input())
	print("ingrese edad ")
	ed = int(input())
	sem = int(input("ingrese semestre matriculado "))
	print("ingrese el numero de materias")
	ma = int(input())
	if s==1:
		if ed>=15 and ed<=25:
			print("ingrese el numero de horas de estudio")
			ho = input()
			print("su grado de estres es =",estres15(sem,ho))
		else:
			if ed>25:
				print("su grado de estres es =",estres25(sem,ma))
			else:
				print("edad incorrecta")
	else:
		if sem<6:
			print("su grado de estres es =",estresm1(ed))
		else:
			print("ingrese el numero de horas de estudio")
			ho = input()
			print("su grado de estres es =",estresm2(ma,ho))

