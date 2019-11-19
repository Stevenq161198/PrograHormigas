import math
import random
from time import time
import multiprocessing

from Combination import *
from misc.ant_admin import AntAdmin
from misc.tree import Tree



def getCombinations(lenTrees):
    combinations = []
    for cant in range(1, lenTrees):
        combinations.append(Combination(cant, generateAnts(cant, lenTrees), 0, 0))
    return combinations


def generateAnts(quant, lenTrees):
    return [index for _ in range(0, quant) for index in range(0, lenTrees)]  # Manda 3 hormigas a cada árbol


def evaluateCombination(combination, maxTime):
    resultTuple = AntAdmin.evaluate(trees, combination.ants, 1, maxTime)
    combination.quantAnts = resultTuple["ant_count"]
    combination.quantLeaf = resultTuple["leaf_count"]
    combination.order = resultTuple["loop"]
    return combination


def probabilistic(trees, maxTime):
    combinations = getCombinations(len(trees))
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
