import math
import random

from Arbol import *
from Rango import *

"""
def sumatoria(tiempo, arboles):
    cantTotalHojas = 0
    cantHormigas = 0
    duracion = len(arboles)
    for arbol in arboles:
        seg = 0
        hojasRecogidas = 0
        while seg < tiempo:
            cantHojas = math.floor((tiempo - seg) / (2 * (arbol.ubicacion + arbol.duracionSubir)))
            if arbol.cantHojas > 0 and cantHojas <= arbol.cantHojas:
                arbol.cantHojas -= cantHojas
                hojasRecogidas += cantHojas
                seg += duracion
            else:
                duracion -= 1
                break
        print("_____________________________________")
        print("Hojas Recogidas", hojasRecogidas)
        cantTotalHojas += hojasRecogidas
        hormigasxIteracion = math.ceil(hojasRecogidas / 2)
        print("Hormigas por Arbol:", hormigasxIteracion)
        cantHormigas += hormigasxIteracion
        print("Total Hormigas: ", cantHormigas)
        print("_____________________________________")
    return cantHormigas, cantTotalHojas

"""
"""
def sumatoria(tiempo, arboles):
    cantTotalHojas = 0
    cantHormigas = 0
    for arbol in arboles:
        seg = 0
        hojasRecogidas = 0
        while seg < math.ceil( tiempo/len(arboles)):
            hojasRecogidas += math.floor((tiempo - seg) / (2 * (arbol.ubicacion + arbol.duracionSubir)))
            seg += 1
        print("Hojas Recogidas",hojasRecogidas)
        cantTotalHojas += hojasRecogidas
        cantHormigas += math.ceil(hojasRecogidas / 2)
        print("Hormigas", cantHormigas)
   - return cantHormigas, cantTotalHojas
   """

"""
def sumatoria(tiempo, arboles):
    cantTotalHojas = 0
    cantHormigas = 0
    for arbol in arboles:
        seg = 0
        hojasRecogidas = 0
        while seg < tiempo:
            hojasRecogidas += math.floor((tiempo - seg) / (2 * (arbol.ubicacion + arbol.duracionSubir)))
            seg += 1
            tiempo -= 1
        print("Hojas Recogidas", hojasRecogidas)
        cantTotalHojas += hojasRecogidas
        cantHormigas += math.ceil(hojasRecogidas / 2)
        print("Hormigas", cantHormigas)
    return cantHormigas, cantTotalHojas
"""


def cantHojas(tiempo, arboles, cantHormigas, rango):
    hojasTotales = 0
    for arbol in arboles:
        seg = 0
        hojasRecogidas = 0
        hojas = arbol.cantHojas
        while seg < tiempo / len(arboles):
            cantHojas = math.floor((tiempo - seg) / (2 * (arbol.ubicacion + arbol.duracionSubir)))
            if hojas > 0 and cantHojas <= hojas and cantHormigas >= 1:
                hojas -= cantHojas
                hojasRecogidas += cantHojas
                cantHormigas -= 1
                seg += 1
            else:
                break
        # print("Hojas Recogidas", hojasRecogidas)
        rango.hojas += hojasRecogidas
    rango.sobrantes = cantHormigas


def sacarRangos(cantRangos, maxHormigas):
    rango = math.floor(maxHormigas / cantRangos)
    rangos = []
    for cant in range(0, cantRangos):
        rangos.append(Rango(1, rango * cant + 1, rango * (cant + 1)))
    return rangos


def probabilista(pCantPruebas, maxHormigas, tiempo, arboles):
    ranges = sacarRangos(15, maxHormigas)
    mejorRango = ranges[random.randint(0, len(ranges) - 1)]
    quantRandomAnts = random.randint(mejorRango.numMinimo, mejorRango.numMaximo)
    cantHojas(tiempo, arboles, quantRandomAnts, mejorRango)
    print("Numero Base: ", quantRandomAnts)
    print("Cantidad Hojas Base: ", mejorRango.hojas)

    for prueba in range(0, pCantPruebas):
        ran = random.uniform(0.0, 1.0)
        for _range in ranges:
            quantRandomAnts = random.randint(_range.numMinimo, _range.numMaximo)
            if _range.probabilidad > ran:
                cantHojas(tiempo, arboles, quantRandomAnts, _range)
                if _range.hojas >= mejorRango.hojas and _range.sobrantes == 0:
                    mejorRango = _range
                    _range.probabilidad += 0.09
                else:
                    _range.probabilidad -= 0.5
    print(ranges)


probabilista(15, 50, 20, [Arbol(2, 2, 100), Arbol(4, 2, 20), Arbol(5, 3, 20), Arbol(8, 3, 20)])
