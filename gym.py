def promedio(x, z):
	pro = x/z #promedio
	return pro

def peso(x):
	i = 0 #contador "
	total=0
	for i in range(1,x+1):
		print("ingrese el peso de la persona  ",i)
		p =int( input())#leo el peso
		total = total+p
		i = i+1
	return total

if __name__ == '__main__':
	print("INGRESE EL TOTAL DE PERSONAS   ")
	n =int( input())#leo el total 
	pe = peso(n)#guarda la variable que retorna la funcion 
	print("el peso total es : ",pe)
	print("el promedio es :",promedio(pe,n))
