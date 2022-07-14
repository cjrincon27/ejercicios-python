cov = {'cundinamarca' :134545,'antioquia' :70340,
               'choco' :456456,'caqueta' :560000,
               'casanare' :34000, 'cauca' :3434000,
                 'cesar' :324342,  'cordoba' :120000,
               'guainia' :23000,'huila' :890000}
print(cov)#mostramos
cov.update(vichada=575567)#agregamos
print()
print(cov)
cov['cundinamarca']=10000000#modificar
print()
print(cov )
cov.pop('antioquia')#eliminar
print()
print(cov )
print()
print('vichada' in cov)#operador in 



              
