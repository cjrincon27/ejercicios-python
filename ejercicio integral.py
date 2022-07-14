from sympy import symbols
from sympy import integrate
x=symbols('x')
def integral(a,b,c):
    fun=a*x**3+b*x**2+c*1
    print(" la funcion es",fun)
    print(" la integral es :",integrate(fun,x))

print("solucion")
integral(43,55,62)