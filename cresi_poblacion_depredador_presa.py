import matplotlib.pyplot as plt
import numpy as np
def f1(t,x,y):
    return (0.4 * x - 0.3 * x * y)
def f2(t,x,y):
    return(-0.37*y + 0.05*x*y)
def euler2(f1,f2,t0,tn,x0,y0,n):
    t=np.linspace(t0,tn,n+1)
    x=np.zeros(n+1)
    y=np.zeros(n+1)
    x[0]=x0
    y[0]=y0
    h=(tn-t0)/n
    for i in range(1,n+1):
        x[i] = x[i-1]+h*f1(t[i-1],x[i-1],y[i-1])
        y[i] = y[i-1]+h*f2(t[i-1],x[i-1],y[i-1])
    return (t,x,y)

(t,x,y)=euler2(f1, f2, 0, 100, 3, 1, 10000)
print(x)
print(y)
fig=plt.figure(1)
plt.ylabel("poblacion(en miles)",color="green")
plt.xlabel("t(años)",color="red")
plt.text(3,16.2,"poblacion de conejos",color="orange")
plt.text(2,3,"poblacion de zorro",color="blue")
plt.title("poblacion de conejos y zorros",color="orange")
plt.grid(True)
plt.plot(t,x,color="orange")
plt.plot(t,y,color="blue")
plt.show()
