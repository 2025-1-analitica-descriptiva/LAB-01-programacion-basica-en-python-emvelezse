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
        col_4 = len(row_values[3].split(","))
        col_5 = len(row_values[4].split(","))
        result.append((row_values[0], col_4, col_5))
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

def pregunta_10():
    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
    sequence = _load_input("files/input/data.csv")
    sequence = mapper_query(sequence)
    return(sequence)
