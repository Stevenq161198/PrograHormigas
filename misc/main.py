from misc.tree import Tree
from misc.ant_admin import *
from misc.html_writer import draw_to_html


trees = [
        Tree("A", 3, 4), # El nombre es opcional, es sólo para que se identifique en el HTML
        Tree("B", 6, 8, 1, 1), # Ahora se puede enviar también el tamaño base y el porcentaje de crecimiento
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

ants = [index for _ in range(0, 3) for index in range(0, len(trees))] # Manda 3 hormigas a cada árbol
AntAdmin.evaluate(trees, ants, 1, 500)