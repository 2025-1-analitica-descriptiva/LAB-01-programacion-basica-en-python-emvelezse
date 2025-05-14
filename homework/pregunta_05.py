"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""

import fileinput
from itertools import groupby

def _load_input(input):
    sequence = []
    with fileinput.input(files=input) as f:
        for line in f:
            sequence.append((fileinput.filename(), line))
    return sequence

def mapper_query(sequence):
    result = []
    for index, (_, row) in enumerate(sequence):
        row_values = row.strip().split("\t")
        result.append((row_values[0], int(row_values[1])))
    return result

def reducer(sequence):
    """Reducer"""
    result = []
    for key, group in groupby(sequence, lambda x: x[0]):
        lista = list(value for _, value in group)
        result.append((key, max(lista), min(lista)))
    return result

def pregunta_05():
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
    sequence = _load_input("files/input/data.csv")
    sequence = mapper_query(sequence)
    sequence = sorted(sequence)
    sequence = reducer(sequence)
    return(sequence)