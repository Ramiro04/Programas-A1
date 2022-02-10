def do_while(funcion = None, condicion = None):
    if not funcion or not condicion:
        return
    else:
        funcion()
        while condicion():
            funcion()
 
i = 0
 
def funcion():
    global i
    i = i + 1
    print(i)
 
def condicion():
    global i
    return i < 3
 
do_while(funcion, condicion)