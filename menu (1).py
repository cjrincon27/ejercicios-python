def cek(x):
	ck = x+273.15
	return ck

def cef(x):
	cf = (x*9/5)+32
	return cf

def fac(x):
	fc = (x-32)*5/9
	return fc

def fak(x):
	fk = (x-32)*5/9+273.15
	return fk

def kec(x):
	kc = x-273.15
	return kc

def kef(x):
	kf = (x-273.15)*9/5+32
	return kf

if __name__ == '__main__':
	print("MENU")
	print("1= celsisus a fahrenheit   y kelvin")
	print("2= fahrenheit  a celsisus y kelvin ")
	print("3=kelvin a celsisus y fahrenheit  ")
	op = float(input())
	if op==1:
		print("ingrese los grados celsius")
		c = int (input()) #leemos celsius
		print("en fahrenheit =",cef(c))
		print("en kelvin=",cek(c))
	elif op==2:
		print("ingrese los grados fahrenheit")
		f =int (input())#leemos fahrenheit  
		print("en celsisus =",fac(f))
		print("en kelvin=",fak(f))
	elif op==3:
		print("ingrese los grados kelvin")
		k = int (input())#leemos kelvin
		print("en celsisus =",kec(k))
		print("en fahrenheit =",kef(k))
	else:
		print("FIN")
