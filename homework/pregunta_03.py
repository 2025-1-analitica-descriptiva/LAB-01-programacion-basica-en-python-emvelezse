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
        result.append((key, sum(value for _, value in group)))
    return result

def shuffle_and_sort(sequence):
    """Shuffle and Sort"""
    return sorted(sequence, key=lambda x: x[0])

def pregunta_03():
    """
    Retorne la suma de la columna 2 por cada letra de la primera columna como
    una lista de tuplas (letra, suma) ordendas alfabeticamente.

    Rta/
    [('A', 53), ('B', 36), ('C', 27), ('D', 31), ('E', 67)]

    """
    sequence = _load_input("files/input/data.csv")
    sequence = mapper_query(sequence)
    sequence = sorted(sequence)
    sequence = reducer(sequence)
    return(sequence)
