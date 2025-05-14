"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""
import glob
import fileinput

def _load_input(input):
    sequence = []
    with fileinput.input(files=input) as f:
        for line in f:
            sequence.append((fileinput.filename(), line))
    return sequence

def mapper_query(sequence):
    """Mapper"""
    result = 0
    for index, (_, row) in enumerate(sequence):
        row_values = row.strip().split("\t")
        print(int(row_values[1]))
        result+=int(row_values[1])
    return result

def pregunta_01():
    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
    sequence = _load_input("files/input/data.csv")
    result = mapper_query(sequence)
    return result

