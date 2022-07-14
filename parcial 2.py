
def perfectos(n):
	k = int()
	ev = int()
	sm=0
	for k in range(2,n+1):
		ev = evaluaperfectos(k)
		if ev==1:
			sm = sm+1
			print(k)
	return sm

def acumulaperfectos(n):
	j = int()
	sp = int()
	e = int()
	for j in range(2,n+1):
		e = evaluaperfectos(j)
		if e==1:
			sp = sp+j
	return sp

def evaluaperfectos(n):
	np = int()
	suma = int()
	i = int()
	res = int()
	for i in range(1,n):
		res = n%i
		if res==0:
			suma = suma+i
	if suma==n:
		np = 1
	else:
		np = 0
	return np

if __name__ == '__main__':
	print("ingrese el numero ")
	num = int(input())
	print("el acomulado de los perfectos hasta ",num," = ",acumulaperfectos(num))
	print("los numeros perfectos hasta",num," son:")
	print("=",perfectos(num))

