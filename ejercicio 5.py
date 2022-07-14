from sympy import *

def derivar(a,b,c):
    x=Symbol('x')
    fun=a*x**2+b*x+c
    print(" la funcion es",fun)
    print(" la derivada es :",diff(fun,x))

print("solucion")
derivar(1,5,6)