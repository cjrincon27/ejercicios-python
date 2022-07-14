materias= ("diferencial", "integral", "multivariable","ecuaciones","circuitos1","circuitos2","mecanica","analitica","materiales","programacion1","programacion 2","catedra")
print("tupla")
print(materias)
#pasamos la tupla a lista
print()
lista=list(materias)
print("lista")
print(lista)
#agregamos elemento
lista.append("ingles")
print()
print("agregamos elemento")
print(lista)
#eliminamos elemento por posicion (0)en este caso
lista.pop(0)
print()
print("eliminamos elemento ")
print(lista)
#modificar elemento
lista[0]="ambiental"
print()
print("modificar elemento ")
print(lista)
