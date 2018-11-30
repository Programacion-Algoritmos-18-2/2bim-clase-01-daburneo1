"""
    Ejecutable de manejo de excepciones
"""

from paquete_excepciones.miexepcion import MiError

bandera = True
x = 0

while bandera: #es lo mismo que While bandera == True
    try:
        x = input("Ingresar valor:\n")
        x = float(x)
        if x < 20: #Si cumple la condicion entra al if y se genera el except
            raise MiError(x)
        bandera = False #Si no entra al if, osea que el numero sea "correcto" bandera se convierte en False y sale del while    
    except MiError as e:
        print(e)
    
    except ValueError as e:
        print("Existe un error, con el valor (%s) ingresado (%s)" % (x, e))


print("Su valor (%s) ingresado cumple las condiciones" % (x))
