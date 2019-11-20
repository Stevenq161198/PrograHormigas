import random

from Chromosomes import *
from misc.ant_admin import AntAdmin


def _generar_padre(longitud, geneSet, antsSpeed, time, trees):
    genes = []
    while len(genes) < longitud:
        genes.append(geneSet[random.randint(0, len(geneSet) - 1)])
    result = AntAdmin.evaluate(trees, genes, antsSpeed, time)
    return Chromosome(genes, result["leaf_count"],result["ant_count"], result["loop"])


def _mutar(padre, geneSet, time, trees):
    index = random.randrange(0, len(padre.Genes))
    geneChild = padre.Genes
    for quantChanges in range(0, 3):
        nuevoGen, alterno, newGene = random.sample(geneSet, 3)
        if nuevoGen == geneChild[index]:
            geneChild[index] = alterno
        else:
            geneChild[index] = nuevoGen
        #geneChild.append(newGene)
    genes = geneChild
    ##Cambiar Velocidad
    result = AntAdmin.evaluate(trees, genes, 1, time)
    return Chromosome(genes, result["leaf_count"],result["ant_count"], result["loop"])


def genetic(longitudObjetivo, aptitudOptima, geneSet, antsSpeed, time, trees):
    random.seed()
    bestDad = _generar_padre(longitudObjetivo, geneSet, antsSpeed, time, trees)
    if bestDad.Aptitud >= aptitudOptima:
        return bestDad
    for i in range(0, 200):
        child = _mutar(bestDad, geneSet, time, trees)
        # print("Mejor Padre",mejorPadre)
        # print("Chico",child)
        if bestDad.Aptitud >= child.Aptitud:
            continue
        if child.Aptitud >= aptitudOptima:
            return child
        bestDad = child
    return bestDad
