"""
Ejemplos de manejo de excepciones
"""

try:
	numero1 = input("Ingrese numero 1: \n")
	numero1 = int(numero1)
	numero2 = input("Ingrese numero 2: \n")
	numero2 = int(numero2)
	operacion =  numero1 / numero2
	print("El valor de la operacion es %d" %(operacion))

except NameError as e:
	print("Existe un error: %s" % e)

except ValueError as e: #Capturar el error en una tipo variable
	print("Existe un error (%s): %s" % (e.__class__, e)) #Tipo de error

except ZeroDivisionError as e:
	print("Existe un error (%s): %s" % (e.__class__, e))

#except Exception as e: #Exception captura todos los tipos de errores, tipo padre
    #print("Existe un error (%s): %s" % (e.__class__, e)) 