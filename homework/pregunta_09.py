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
        row_1 = row_values[4].split(",")
        for word in row_1:
            lista_letter = word.split(":")
            result.append((lista_letter[0], 1))
    return result

def reducer(sequence):
    """Reducer"""
    result = {}
    for key, group in groupby(sequence, lambda x: x[0]):
        result[key]= (sum(value for _, value in group))
    return result


def pregunta_09():
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
    sequence = _load_input("files/input/data.csv")
    sequence = mapper_query(sequence)
    sequence = sorted(sequence)
    sequence = reducer(sequence)
    return(sequence)
