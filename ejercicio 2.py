import matplotlib.pyplot as plt
import numpy as np
#generar el plano
x=np.linspace(-np.pi,np.pi)
#generar los datos
y1=np.sin(x)
y2=np.cos(x)
#generar la grafica
plt.plot(x,y1,x,y2)
#mostrar la grafica
plt.show()
