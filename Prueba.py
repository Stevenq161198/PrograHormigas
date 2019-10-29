import math
import random
from time import time
import multiprocessing

from Arbol import *
from Rango import *

def voraz(tiempo, arboles):
    v = multiprocessing.current_process()
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


def sacarRangos(cantRangos, maxHormigas):
    rango = math.floor(maxHormigas / cantRangos)
    rangos = []
    for cant in range(0, cantRangos):
        rangos.append(Rango(1, rango * cant + 1, rango * (cant + 1)))
    return rangos


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
    p = multiprocessing.current_process()
    tiempo = 100000
    while tiempo > 0:
        hojasSolicitadas = 5000000
        arboles = [Arbol(2, 2, 1500000), Arbol(4, 2, 5000000), Arbol(5, 3, 2500000), Arbol(8, 3, 250000)]
        mejorRango = probabilista(1500, tiempo, arboles)
        print(mejorRango)
        print(tiempo)
        if hojasSolicitadas - hojasSolicitadas *0.05 < mejorRango.hojas < hojasSolicitadas:
            return print(mejorRango)
        tiempo -= round(tiempo * 0.020)

if __name__ == "__main__":

    start_time = time()
    voraz = multiprocessing.Process(name='voraz', target=voraz, args=(30, [Arbol(2, 2, 1000), Arbol(4, 2, 500000), Arbol(5, 3, 250000), Arbol(8, 3, 250000)]))
    mainProba = multiprocessing.Process(name='mainProba', target=mainProba)

    voraz.start()
    mainProba.start()

    voraz.join()
    mainProba.join()

    elapsed_time = time() - start_time
    print("Elapsed time: %.10f seconds." % elapsed_time)
