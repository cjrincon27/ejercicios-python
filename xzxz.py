
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

