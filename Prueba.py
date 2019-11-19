import math
import random
from time import time
import multiprocessing

from Arbol import *
from Combinaciones import *
from misc.ant_admin import AntAdmin
from misc.tree import Tree


def voraz(tiempo, arboles):
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
    print("hormigas: ", cantHormigas, "Hojas", cantTotalHojas)
    return cantHormigas, cantTotalHojas


def cantHojas(tiempo, arboles, cantHormigas, rango):
    rango.hojas = 0
    for arbol in arboles:
        seg = 0
        hojas = arbol.cantHojas
        while seg < tiempo:
            cantHojas = math.floor((tiempo - seg) / (2 * (arbol.ubicacion + arbol.duracionSubir)))
            if hojas > 0 and cantHormigas >= 1:
                if cantHojas <= hojas:
                    hojas -= cantHojas
                    rango.hojas += cantHojas
                else:
                    rango.hojas += hojas
                    hojas = 0
                cantHormigas -= 1
                seg += 1
                tiempo -= 1
            else:
                break
    rango.sobrantes = cantHormigas


def sacarCombinaciones(lenTrees):
    combinations = []
    for cant in range(1, lenTrees):
        combinations.append(Combination(cant, generateAnts(cant, lenTrees), 0, 0))
    return combinations


"""
def probabilista(maxHormigas, tiempo, arboles):
    ranges = sacarRangos(25, maxHormigas)
    mejorRango = ranges[random.randint(0, len(ranges) - 1)]
    quantRandomAnts = random.randint(mejorRango.numMinimo, mejorRango.numMaximo)
    cantHojas(tiempo, arboles, quantRandomAnts, mejorRango)
    for prueba in range(0, 10):
        ran = random.uniform(0.0, 1.0)
        for _range in ranges:
            quantRandomAnts = random.randint(_range.numMinimo, _range.numMaximo)
            if _range.probabilidad > ran:
                cantHojas(tiempo, arboles, quantRandomAnts, _range)
                if _range.hojas >= mejorRango.hojas and _range.sobrantes <= _range.numMaximo - _range.numMinimo:
                    mejorRango = _range
                    _range.probabilidad += 0.09
                else:
                    _range.probabilidad -= 0.5
    return mejorRango


def mainProba():
    tiempo = 100000
    while tiempo > 0:
        hojasSolicitadas = 5000000
        arboles = [Arbol(2, 2, 1500000), Arbol(4, 2, 5000000), Arbol(5, 3, 2500000), Arbol(8, 3, 250000)]
        mejorRango = probabilista(1500, tiempo, arboles)
        print(mejorRango)
        print(tiempo)
        if hojasSolicitadas - hojasSolicitadas * 0.05 < mejorRango.hojas < hojasSolicitadas:
            return print(mejorRango)
        tiempo -= round(tiempo * 0.020)
"""


def generateAnts(quant, lenTrees):
    return [index for _ in range(0, quant) for index in range(0, lenTrees)]  # Manda 3 hormigas a cada árbol


def evaluateCombination(combination, maxTime):
    resultTuple = AntAdmin.evaluate(trees, combination.ants, 1, maxTime)
    combination.quantAnts = resultTuple["ant_count"]
    combination.quantLeaf = resultTuple["leaf_count"]
    combination.order = resultTuple["loop"]
    return combination


def probabilistic(trees, maxTime):
    combinations = sacarCombinaciones(len(trees))
    bestCombination = combinations[random.randint(0, len(combinations) - 1)]
    evaluateCombination(bestCombination, maxTime)
    for prueba in range(0, 5):
        ran = random.uniform(0.0, 1.0)
        for _combination in combinations:
            if _combination.probability > ran:
                evaluateCombination(_combination,maxTime)
                if _combination.quantLeaf >= bestCombination.quantLeaf and _combination.quantAnts <= bestCombination.quantAnts:
                    bestCombination = _combination
                    _combination.probability += 0.09
                else:
                    _combination.probability -= 0.5
    return bestCombination


if __name__ == "__main__":
    start_time = time()
    trees = [
        Tree("A", 3, 4),  # El nombre es opcional, es sólo para que se identifique en el HTML
        Tree("B", 6, 8, 1, 1),  #  Ahora se puede enviar también el tamaño base y el porcentaje de crecimiento
        Tree("C", 6, 6),
        Tree("D", 10, 3),
        Tree("E", 10, 3),
        Tree("F", 11, 5),
        Tree("G", 17, 7),
        Tree("H", 17, 3),
        Tree("I", 18, 2),
        Tree("J", 20, 1),
        Tree("K", 23, 18),
        Tree("L", 25, 2)
    ]
    print("Best Combination:", probabilistic(trees,500))
    elapsed_time = time() - start_time
    print("Elapsed time: %.10f seconds." % elapsed_time)
