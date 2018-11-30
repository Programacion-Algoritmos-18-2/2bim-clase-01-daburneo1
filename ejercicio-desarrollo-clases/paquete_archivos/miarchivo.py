import codecs

class MiArchivo:

    def __init__(self):
        self.archivo = codecs.open("data/informacion.csv", "r")


    def obtener_informacion(self):
        return self.archivo.readlines()

    def cerrar_archivo(self):
        self.archivo.close()

class MiArchivoEscribir:

    def __init__(self):

        self.archivo = codecs.open("data/promedios.csv", "a")

    def agregar_informacion(self, p):
        self.archivo.write("%s - %f\n" % (p.nombre, p.calcular_promedio()))

    def cerrar_archivo(self):
        self.archivo.close()

