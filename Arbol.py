class Arbol:

    def __init__(self, pUbicacion, pDuracionSubir,pProbabilidad):
        self.ubicacion = pUbicacion
        self.duracionSubir = pDuracionSubir
        self.probabilidad = pProbabilidad

    def __repr__(self):
        return '{}: {} {}'.format(self.__class__.__name__,
                                  self.ubicacion, self.duracionSubir)
