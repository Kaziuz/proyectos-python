# Este programa se encarga de generar turnos para un departamento elegido por el usuario

from numeros import *

import os
import platform

finalizar = False
turno_p = generador_perfumeria()
turno_f = generador_farmacia()
turno_c = generador_cosmeticos()


def limpiar_consola():
    # Limpio la consola
    system = platform.system()  # obtengo el sistema operativo
    if system == "Darwin" or system == "Linux":
        os.system("clear")
    else:
        os.system("cls")  # Windows


def bienvenida():
    # Esta función se encarga de mostrar un mensaje de bienvenida al usuario
    print("*" * 50)
    print("*" * 7 + " Bienvenido a la farmacia Python " + "*" * 10)
    print("*" * 50)


def tabla_departamentos():
    # Muestra un mensaje para seleccionar un turno a generar
    print("\nPara cual departamento va ?:")
    print("""
        Escriba [p] para Perfumería
        Escriba [f] para Farmacia
        Escriba [c] para Cosméticos
    """)


def tabla_nuevo_turno():
    # Muestra un mensaje para generar un turno o finalizar el programa
    print("Seleccione una de las siguientes opciones para continuar:")
    print("""
            Escriba [g] para generar otro turno
            Escriba [f] para finalizar el programa
        """)


def opciones_posibles(*args):
    # Genera una lista con las opciones que el usuario debe ingresar para continuar
    lista_opciones = []
    for letra in args:
        lista_opciones.append(letra.lower())
    return lista_opciones


def leer_opt(mensaje, opciones, tabla):
    # Lee la opción ingresada por el usuario y válida la opción hasta que sea correcta
    while True:
        opt = input(mensaje)
        if opt.lower() in opciones:
            break
        else:
            limpiar_consola()
            tabla()
            print("Opción incorrecta. Vuelva a ingresar una opción \n")
    return opt.lower()


def decorar_turno(turno):
    # Agregar un mensaje antes y después del turno generado
    turno_decorado = mensaje_turno(turno)
    return turno_decorado()


def generar_turno(opt):
    # Esta función se encarga de decorar el mensaje del turno generado
    # agregándole un mensaje antes y después
    if opt == "p":
        # Perfumería
        turno = next(turno_p)
        return turno
    elif opt == "f":
        # Farmacia
        turno = next(turno_f)
        return turno
    else:
        # Cosméticos
        turno = next(turno_c)
        return turno


limpiar_consola()
bienvenida()

while not finalizar:
    tabla_departamentos()
    opciones_posibles = opciones_posibles("p", "f", "c")
    opciones_leidas = leer_opt("Escriba una letra para generar su turno: ", opciones_posibles,
                               tabla_departamentos)
    turno_generado = generar_turno(opciones_leidas)
    mostrar_turno_generado = decorar_turno(turno_generado)
    limpiar_consola()
    print(mostrar_turno_generado)
    tabla_nuevo_turno()
    seguir_finalizar = opciones_posibles("f", "g")
    opciones_finales = leer_opt("Escriba una opción del tablero: ", seguir_finalizar, tabla_nuevo_turno)

    if opciones_finales == "g":
        limpiar_consola()
        finalizar = False
    else:
        # Finaliza programa
        finalizar = True
        break

print("Ha salido del programa de generador de turnos")
