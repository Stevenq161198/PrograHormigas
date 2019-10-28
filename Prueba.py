import math

from Arbol import *


def voraz(tiempo, arboles):
    cantTotalHojas = 0
    cantHormigasTotal = 0
    for arbol in arboles:
        seg = 0
        hojasRecogidas = 0
        while seg < tiempo:
            hojasRecogidas += math.floor((tiempo - seg) / (2 * (arbol.ubicacion + arbol.duracionSubir)))
            seg += len(arboles)
        cantTotalHojas += hojasRecogidas
        cantHormigasTotal += math.ceil(hojasRecogidas / 2)
    return cantHormigas, cantTotalHojas


def selected(tiempo, arboles):
    cantTotalHojas = 0
    cantHormigas = 0
    for arbol in arboles:
        seg = 0
        hojasRecogidas = 0
        while seg < tiempo:
            hojasRecogidas += math.floor((tiempo - seg) / (2 * (arbol.ubicacion + arbol.duracionSubir)))
            seg += len(arboles)
        cantTotalHojas += hojasRecogidas
        cantHormigas += math.ceil(hojasRecogidas / 2)
    return cantHormigas, cantTotalHojas


def set_probability(self, prob):
        self.probability = prob

def probabilistic(tiempo,arboles):
    cantTotalHojas = 0
    cantHormigas = 0
    arbolesPosibles = []
    while seg < tiempo:
        rand_index = random.randint(0.1,6.0)
        for arbol in arboles:
            if arboles[2] #por cada arbol que evalue el 2do parametro, si es mayor al rand_index entonces le baja 0.5 
                          #a la probabilidad del arbol (sería al 3era parametro) y si fuera menor al rand_index le suma 0.5
                          # de ahí los manda a evaluar con respecto a la probabilidad que tiene cada uno

if __name__ == "__main__":
    print("Voraz")
    print(voraz(30, [Arbol(2, 2), Arbol(4, 2),Arbol(5, 1)],10))
    print("------------------------")
    print("Selectivo")
    print(selected(30, [Arbol(2, 2)]),10)
    print(probabilistic(30, [Arbol(2, 2), Arbol(4, 2),Arbol(5, 1)], 10))