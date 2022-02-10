#Divide la cadena solo en la primera aparición:

import re

txt = "The rain in Spain"
x = re.split("\s", txt, 3)
print(x)