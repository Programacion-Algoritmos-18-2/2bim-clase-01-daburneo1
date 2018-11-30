"""
    Manejo de Excepciones
    Crear cualquier numero de exceptiones siempre que ereden de una clase como esta
"""

class MiError(Exception):
    """
    """

    def __init__(self, valor):
        self.valor = valor

    def __str__(self):
        return "Error, el valor ingresado %s no es correcto" %(self.valor)
