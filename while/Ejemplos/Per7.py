#Imprima la posición (posición inicial y final) de la primera aparición del partido.
#La expresión regular busca cualquier palabra que comience con una "S" mayúscula:

import re

txt = "The rain in Spain"
x = re.search(r"\br\w+", txt)
print(x.span())