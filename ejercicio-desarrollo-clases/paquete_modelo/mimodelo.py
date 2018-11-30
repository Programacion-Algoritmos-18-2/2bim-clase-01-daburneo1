class Persona(object):
    def __init__(self, n, n1, n2, n3):

        self.nombre = n
        self.nota1 = float(n1)
        self.nota2 = float(n2)
        self.nota3 = float(n3)
        self.promedio = 0.0

    def agregar_nombre(self, n):
        self.nombre = n

    def obtener_nombre(self):
        return self.nombre

    def agregar_nota1(self, n1):
        self.nota1 = float(n1)

    def obtener_nota1(self):
        return self.nota1

    def agregar_nota2(self, n2):
        self.nota2 =  float(n2)

    def obtener_nota2(self):
        return self.nota2
    
    def agregar_nota3(self, n3):
        self.nota3 =  float(n3)

    def obtener_nota3(self):
        return self.nota3

    def calcular_promedio(self):
        promedio = ((self.obtener_nota1() + self.obtener_nota2() + self.obtener_nota3())/3)
        return promedio

    def __str__(self):
        cadena = "El estudiante %s, tiene un promedio de: %f" % (self.nombre, self.calcular_promedio())
        return cadena

