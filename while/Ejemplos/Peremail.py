# Módulo para usar expresiones regulares.
import re
# Módulo para usar objetos fecha
import datetime

# Queremos capturar información de voluntarios para un causa social.
# Debemos saber, para cada voluntario, la siguiente infomación. Ninguno
# de los datos debe omitirse. Además, aplican las siguientes validaciones
# específicas.


# Correo electronico (correo_electronico)
#       - Debe tener formato de correo válido
#       - Debe tener un máximo de 50 posiciones
while True:
    correo_electronico=input("Dame el correo electrónico: ")
    if (correo_electronico==""):
        print("El correo electrónico no se puede omitir.")
    else:
        if not (re.match("^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$",correo_electronico)):
            print("Sólo se permiten correos válidos")
        else:
            break
