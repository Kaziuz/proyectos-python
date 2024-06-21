# Buscador de numeros de serie

import math
import re
import os
from pathlib import Path
import datetime
import time

inicio = time.time()

def comprobar_serie(patron, name_file):
    # Comprueba que la serie ingresada haga match con este formato
    # - [N] + [tres caracteres de texto] + [-] + [5 números]
    # ejemplo: Nryu-12365
    busqueda = re.findall(r"[A-Z][a-z]{3}-\d{5}", patron)
    if len(busqueda) > 0:
        return (name_file, busqueda[0])


def buscar_series(path):
    lista_codigos = []
    for carpeta, subcarpeta, archivo in os.walk(path):
        for arch in archivo:
            if arch:
                ruta_archivo = Path(carpeta) / arch
                try:
                    archivo_crudo = open(ruta_archivo, mode="r", encoding="latin1")
                    read_file = archivo_crudo.read()
                    codigos = comprobar_serie(read_file, arch)
                    if codigos:
                        lista_codigos.append(codigos)
                    archivo_crudo.close()
                except FileNotFoundError:
                    print(f"No se pudo leer el archivo: {path}")
    return lista_codigos


def genear_fecha():
    fecha = datetime.datetime.now()
    year = fecha.year
    mes = fecha.month
    dia = fecha.day
    return f"{dia}/{mes}/{year}"


ruta_proyecto = "/Users/alex/Documents/udemy-python/9.buscador_numeros_serie/buscador_numeros_serie/Mi_Gran_Directorio"
codigos_encontrados = buscar_series(ruta_proyecto)
total_codigos_encontrados = len(codigos_encontrados)
final = time.time()
duracion_busqueda = final - inicio
duracion_redondeada = math.ceil(duracion_busqueda)
print("-" * 50)
print("Fecha de búsqueda: ", genear_fecha(), "\n")
print("ARCHIVO", "\tNRO. Serie")
print("-" * 7, "\t----------\n")
for archivo, serie in codigos_encontrados:
    print(f"{archivo} \t{serie}")
print("\nNúmeros encontrados: {}".format(total_codigos_encontrados))
print("Duración de la búsqueda: ", duracion_redondeada)
print("-" * 50)

