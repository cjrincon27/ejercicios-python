def fdinero(a, b, c):
	i = 0
	j = 0
	k = 0
	dc1=0
	dc2=0
	dc3=0
	for i in range(1,a+1):
		if i%50==0:
			dc1 = dc1+1
	for j in range(1,b+1):
		if j%50==0:
			dc2 = dc2+1
	for k in range(1,c+1):
		if k%50==0:
			dc3 = dc3+1
	print("el dinero del c1=",dc1*50)
	print("el dinero del c2=",dc2*50)
	print("el dinero del c3=",dc3*50)

def fporcentaje(a, b, c, to):
	p1 = (a/to)*100
	p2 = (b/to)*100
	p3 = (c/to)*100
	print("el porcentaje de votos del c1 =",p1," %")
	print("el porcentaje de votos del c2 =",p2," %")
	print("el porcentaje de votos del c3 =",p3," %")
	
def ftotal(a, b, c):
	tv = a+b+c
	return tv


c1 = 38365
c2 = 54821
c3 = 65897
total = ftotal(c1,c2,c3)
print("============cambia colombia ============")
print("el total de los votos es =",total)
print("============================================")
fporcentaje(c1,c2,c3,total)
print("============================================")
fdinero(c1,c2,c3)

