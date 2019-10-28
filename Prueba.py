import math

from Arbol import Arbol


def sumatoria(tiempo, arboles):
    cantTotalHojas = 0
    cantHormigas = 0
    for arbol in arboles:
        seg = 0
        hojasRecogidas = 0
        while seg < tiempo:
            hojasRecogidas += math.floor((tiempo - seg) / (2 * (arbol.ubicacion + arbol.duracionSubir)))
            seg += 2
        print("Hojas Recogidas",hojasRecogidas)
        cantTotalHojas += hojasRecogidas
        cantHormigas += math.ceil(hojasRecogidas / 2)
        print("Hormigas", cantHormigas)
    return cantHormigas, cantTotalHojas


print(sumatoria(12, [Arbol(2, 2), Arbol(4, 2)]))
