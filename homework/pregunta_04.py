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
        month = row_values[2].split("-")[1]
        result.append((month, 1))
    return result

def reducer(sequence):
    """Reducer"""
    result = []
    for key, group in groupby(sequence, lambda x: x[0]):
        result.append((key, sum(value for _, value in group)))
    return result

def pregunta_04():
    """
    La columna 3 contiene una fecha en formato `YYYY-MM-DD`. Retorne la
    cantidad de registros por cada mes, tal como se muestra a continuación.

    Rta/
    [('01', 3),
     ('02', 4),
     ('03', 2),
     ('04', 4),
     ('05', 3),
     ('06', 3),
     ('07', 5),
     ('08', 6),
     ('09', 3),
     ('10', 2),
     ('11', 2),
     ('12', 3)]

    """
    sequence = _load_input("files/input/data.csv")
    sequence = mapper_query(sequence)
    sequence = sorted(sequence)
    sequence = reducer(sequence)
    return(sequence)
    
