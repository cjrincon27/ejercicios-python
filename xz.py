# Este codigo ha sido generado por el modulo psexport 20180802-w32 de PSeInt.
# Es posible que el codigo generado no sea completamente correcto. Si encuentra
# errores por favor reportelos en el foro (http://pseint.sourceforge.net).


# En python no hay forma de elegir como pasar una variable a una
# funcion (por referencia o por valor). Las variables "inmutables"
# (str, int, float, bool) se pasan siempre por copia mientras que
# las demas (listas, objetos, etc.) se pasan siempre por referencia.
# Esto coincide con el comportamiento por defecto en pseint, pero
# cuando utiliza las palabras clave "Por Referencia" para
# alterarlo la traducción no es correcta.

def xz(a, b):
	if a<b:
		i = 0
		total = 0
		for i in range(a,b+1):
			total = total+i
	else:
		if a<b:
			i = 1
			total = 1
			for i in range(a,b+1):
				total = total*i
		else:
			total = 0
	return total

def sumaxz(a, b):
	i = 0
	suma = 0
	for i in range(a,b+1):
		suma = suma+i
	return suma

def productoxz(a, b):
	i = 1
	producto = 1
	for i in range(a,b+1):
		producto = producto*i
	return producto

if __name__ == '__main__':
	x = 2
	z = 3
	print("sumaxz=",sumaxz(x,z))
	print("producto xz=",productoxz(x,z))
	print("xz=",xz(x,z))

