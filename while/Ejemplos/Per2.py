import re
# Busca el primer carácter de espacio en blanco de la cadena:
txt = "Therain in Spain"
x = re.search("\s", txt)

print("El primer espacio en blanco es localizado en posición:", x.start())