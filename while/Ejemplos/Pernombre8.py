# Módulo que permite usar expresiones regulares.
import re

# Ciclo infinito.
while True:
    nombre=input("Dame el nombre: ")
    # Si el valor capturado en rfc hace match con la expresion regular (re.search)...
    if (re.search(r'^[a-zA-Z]{8}',nombre)):

        # usar r'expresion_regular' es muy efectivo.
        # la r indica Raw String, lo que causa que no se interpreten
        # \ como secuencias de escape.

        # anuncia que es válido
        print("Es un Nombre válido.")
        # se sale del ciclo
        break
    else:
        # De lo contrario, anuncia que no es válido, y vuelve a preguntar
        print("No es un Nombre válido. Intenta de nuevo.")