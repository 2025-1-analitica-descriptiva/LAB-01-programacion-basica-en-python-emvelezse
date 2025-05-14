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
        result.append((row_values[0], row_values[1]))
    return result

def reducer(sequence):
    """Reducer"""
    order_sequence = []
    for i in sequence:
        if not i in order_sequence:
            order_sequence.append(i)
    result = []
    for key, group in groupby(order_sequence, lambda x: x[1]):
        result.append((int(key), sorted([letter[0] for letter in group])))
    return result

def shuffle_and_sort(sequence):
    """Shuffle and Sort"""
    return sorted(sequence, key=lambda x: x[1])

def pregunta_08():
    """
    Genere una lista de tuplas, donde el primer elemento de cada tupla
    contiene  el valor de la segunda columna; la segunda parte de la tupla
    es una lista con las letras (ordenadas y sin repetir letra) de la
    primera  columna que aparecen asociadas a dicho valor de la segunda
    columna.

    Rta/
    [(0, ['C']),
     (1, ['B', 'E']),
     (2, ['A', 'E']),
     (3, ['A', 'B', 'D', 'E']),
     (4, ['B', 'E']),
     (5, ['B', 'C', 'D', 'E']),
     (6, ['A', 'B', 'C', 'E']),
     (7, ['A', 'C', 'D', 'E']),
     (8, ['A', 'B', 'D', 'E']),
     (9, ['A', 'B', 'C', 'E'])]

    """
    sequence = _load_input("files/input/data.csv")
    sequence = mapper_query(sequence)
    sequence = shuffle_and_sort(sequence)
    sequence = reducer(sequence)
    return sequence
pregunta_08()
