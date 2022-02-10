#Realice una búsqueda que devuelva un objeto de coincidencia:

import re

txt = "The rain in Spain"
x = re.search("ai", txt)
print(x) #this will print an object