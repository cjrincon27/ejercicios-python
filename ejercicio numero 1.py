def promediopesos(a, b):
	promedio= a/b 
	return promedio

def  totalpesos(a):
	i = 0 
	sumapesos=0
	for i in range(1,a+1):
		print("peso de la persona ",i,"=")
		peso =int( input())
		sumapesos = sumapesos+peso
		i = i+1
	return sumapesos

if __name__ == '__main__':
	print("total de participantes  =")
	participantes =int( input())
	x = totalpesos(participantes)
	print("el acomulado de los pesos es =  ",x)
	print("el promedio de los pesos es =",promediopesos(x,participantes))
