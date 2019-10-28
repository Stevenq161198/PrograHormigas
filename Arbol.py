class Arbol:

    def __init__(self, pUbicacion, pDuracionSubir):
        self.ubicacion = pUbicacion
        self.duracionSubir = pDuracionSubir

    def __repr__(self):
        return '{}: {} {}'.format(self.__class__.__name__,
                                  self.ubicacion, self.duracionSubir)
