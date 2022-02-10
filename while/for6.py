cadena = "Mercurio,Venus,Tierra,Marte"
print(cadena)
lista_planetas = cadena.split(',')
print (lista_planetas)
for planeta in lista_planetas:
	print (planeta)
lista_planetas.sort()
print(lista_planetas)
cadena2=",".join(lista_planetas)
print(cadena2)