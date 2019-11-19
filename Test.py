import math
import random
from time import time
import multiprocessing

from Combination import *
from misc.ant_admin import AntAdmin
from misc.tree import Tree

antSpeed = 1


def oneByOne(timeLapse, trees, start_time):
    global antSpeed
    totalLeaves = 0
    while time() - start_time < timeLapse:
        cantAnts = 0
        totalLeaves = 0
        for tree in trees:
            timeElapsed = 2 * ((tree.x / antSpeed) + (tree.height / antSpeed))
            cantAnts = math.floor(math.floor(timeElapsed) * (1 / antSpeed))
            leavesXTree = math.floor(tree.leaves_count / cantAnts) * cantAnts
            totalLeaves += leavesXTree
        print("Cantidad Hormigas: ", cantAnts)
        print("Hojas Totales: ", totalLeaves)
        return cantAnts


#################################################################################

def getBacks(trees):
    allBacks = 0
    for tree in trees:
        allBacks += tree.total_distance
    return allBacks


def getProbability(trees, allBacks):
    probabilities = []
    totalProb = 0
    for tree in trees:
        prob = 1 - tree.total_distance / allBacks
        probabilities.append(prob)
        totalProb += prob
    for index in range(0, len(probabilities)):
        probabilities[index] = probabilities[index] / totalProb
    return probabilities


def getTreeByProbability(random, probabilities):
    treePosition = 0
    for probability in probabilities:
        if random <= 0 or treePosition >= len(probabilities) - 1:
            break
        treePosition += 1
        random -= probability
    return treePosition


def probabilistic(quantAnts, probabilities, trees, time):
    ants = []
    for i in range(0, quantAnts):
        r = random.uniform(0.0, 1.0)
        position = getTreeByProbability(r, probabilities)
        ants.append(position)
    print(ants)
    result = AntAdmin.evaluate(trees, ants, antSpeed, time)
    return result


def mainProbabilistic(trees, start_time, time):
    quantAnts = oneByOne(500, trees, start_time)
    allBacks = getBacks(trees)
    probabilities = getProbability(trees, allBacks)
    bestResult = probabilistic(quantAnts, probabilities, trees, time)
    print("Probabilities",probabilities)
    for test in range(0, 15):
        result = probabilistic(quantAnts, probabilities, trees, time)
        if result["leaf_count"] > bestResult["leaf_count"]:
            bestResult = result
    print(bestResult)
    return bestResult


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
if __name__ == "__main__":
    start_time = time()
    mainProbabilistic(trees, start_time, 500)
    elapsed_time = time() - start_time
    print("Elapsed time: %.10f seconds." % elapsed_time)
