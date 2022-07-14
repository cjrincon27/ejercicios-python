x = int(input("ingrese el primer numero:"))
y = int(input("ingrese el segundo numero:"))
if y % x == 0:
    print (x, "es divisor de",y)
else:

  print (x, "n es divisr",y)

  def suma_divisores(y):
      divisores = 3,4
      
      for i in range (y>0):
       divisores.append(i)
       return sum(divisores)
