import json
import math
import string

from Genetic import *
from Probabilistic import mainProbabilistic
from misc.tree import Tree

import json

antSpeed = 1


def oneByOne(pTrees):
    global antSpeed

    cantAnts = 0
    totalLeaves = 0
    for tree in pTrees:
        timeElapsed = 2 * ((tree.x / antSpeed) + (tree.height / antSpeed))
        cantAnts = math.floor(math.floor(timeElapsed) * (1 / antSpeed))
        leavesXTree = math.floor(tree.leaves_count / cantAnts) * cantAnts
        totalLeaves += leavesXTree
    print("Cantidad Hormigas: ", cantAnts)
    print("Hojas Totales: ", totalLeaves)
    return cantAnts, totalLeaves


def getGrowPercentage(pTreeLength, pTreeLevels, pLeafLength):
    return (pLeafLength/pTreeLength)**1/pTreeLevels
trees = []
with open('test3.json') as json_file:
    data = json.load(json_file)
    indexLetras = 0
    for p in data['test']:
        # print('PosX: ' + str(p['posX']))
        # print('Length: ' + str(p['length']))
        # print('Levels: ' + str(p['levels']))
        # print('LeafLength: ' + str(p['leafLength']))
        # print('')
        growPercentage = getGrowPercentage(p['length'],p['levels'],p['leafLength'])
        tree = Tree("A", p['posX'], p['levels'], p['length'],growPercentage)
        # tree = Tree("A", p['posX'], p['levels'])
        trees.append(tree)
        indexLetras += 1

"""trees = [
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
"""

if __name__ == "__main__":
    geneSet = generateGeneSet(trees)
    tiempo = int(input("Digite el tiempo por favor: "))
    quantAntsOO = oneByOne(trees)
    start_timeG = time()
    print("Genetic: ",genetic(quantAntsOO[0], quantAntsOO[1], geneSet, antSpeed, 100000000000, trees, start_timeG, (tiempo * 0.2)))
    elapsed_time = time() - start_timeG
    print("Elapsed time: %.10f seconds." % elapsed_time)

    start_timeP = time()
    print("Probabilistic: ",mainProbabilistic(trees, quantAntsOO[0], start_timeP, 100000000000, (tiempo * 0.2)))
    elapsed_time = time() - start_timeP
    print("Elapsed time: %.10f seconds." % elapsed_time)
    """
    mainProbabilistic(trees, quantAntsOO[0], start_time, 900000, (tiempo * 0.2))
    print("Mejor",genetic(quantAntsOO[0], quantAntsOO[1], geneSet, antSpeed, 900000, trees, start_time, (tiempo * 0.2)))
    """
    mainProbabilistic = multiprocessing.Process(target=mainProbabilistic, args=(trees, quantAntsOO[0], start_time, 900000, (tiempo * 0.2)))
    genetic = multiprocessing.Process(target=genetic, args=(quantAntsOO[0], quantAntsOO[1], geneSet, antSpeed, 900000, trees, start_time, (tiempo * 0.2)))
    mainProbabilistic.start()
    genetic.start()
    mainProbabilistic.join()
    genetic.join()
    
    elapsed_time = time() - start_time
    print("Elapsed time: %.10f seconds." % elapsed_time)
    """
