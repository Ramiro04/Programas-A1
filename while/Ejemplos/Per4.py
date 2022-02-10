#Reemplace cada carácter de espacio en blanco con el número 9:

import re

txt = "The rain    in    Spain"
x = re.sub("\s", "9", txt)
print(x)