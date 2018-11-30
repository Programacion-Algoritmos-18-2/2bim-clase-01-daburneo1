"""
Ejemplos de manejo de excepciones
"""

try:
 	edad = input("Ingrese su edad: \n")
 	edad = int(edad)
 	print("Su edad es: %d" %(edad))
except NameError as e:
	print("Existe un error: %s" % e)

#except ValueError as e: #Capturar el error en una tipo variable
#	print("Existe un error (%s): %s" % (e.__class__, e)) #Tipo de error

except Exception as e: 
    print("Existe un error (%s): %s" % (e.__class__, e)) 