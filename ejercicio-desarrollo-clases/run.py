from paquete_archivos.miarchivo import MiArchivo, MiArchivoEscribir
from paquete_modelo.mimodelo import Persona

m = MiArchivo() # metodo para leer el archivo
m2 = MiArchivoEscribir() # metodo para escribir el archivo

lista = m.obtener_informacion()
lista = [l.split("|") for l in lista] #Separar

lista = lista[1:]
for d in lista:
    #print(d)
    p = Persona(d[0], d[1], d[2], d[3])
    print(p)
    m2.agregar_informacion(p)

m.cerrar_archivo()
m2.cerrar_archivo()