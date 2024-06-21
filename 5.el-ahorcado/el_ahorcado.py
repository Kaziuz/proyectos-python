from random import choice

def elegir_palabra():
    # Definimos una lista de palabras y seleccionamos una al azar
    palabras = ["patineta", "aguardiente", "cerveza", "sancocho", "yucas", "espirulina","python", "esternocleido"]
    palabra = choice(palabras)
    return palabra


def mostrar_guiones(palabra):
    guiones = []
    for l in palabra:
        guiones.append("-")
    return guiones


def pedir_letra():
    letra = input("Ingrese una letra: ")
    return letra.lower()


def ingresa_letra(letra):
    # Verificamos que solo sea un letra, que no sea un numero ni caracteres especiales
    if letra.isnumeric():
        print("\n")
        print("No se permiten números")
        return False
    elif len(list(letra)) > 1:
        print("\n")
        print("No se puede ingresar mas de una letra")
        return False
    elif not letra.isalpha():
        print("\n")
        print("Eso no es una letra")
        return False
    else:
        return True
    
    
def validar_letra(letra):
    # Pedimos una letra hasta que sea una sola letra
    while ingresa_letra(letra) == False:
        letra = pedir_letra()
    return letra


def esta_letra_en_palabra(letra, palabra):
    # Verificamos si la letra ingresada por el usuario si esta en la palabra elegida por el sistema
    index_letra_palabra = palabra.find(letra)
    if (index_letra_palabra >= 0):
        return True
    else:
        return False
    
    
def mostrar_guiones_correctos(letra, palabra, guiones):
    # reemplazamos la letra ingresada por su posición en la lista de guiones
    for indice, l in enumerate(palabra):
        if letra == l:
            guiones[indice] = letra_valida
    return guiones


def completo_palabra(guiones):
    # Verificamos si la lista de guiones fue reemplazada por letras
    if "".join(guiones).count("-") > 0:
        return False
    else:
        return True


# ----------------------------------------------------
# INICIA EL JUEGO: EL AHORCADO
letras_incorrectas = []
vidas = 7
palabra_seleccionada = elegir_palabra()
guiones = mostrar_guiones(palabra_seleccionada)

print(f"La palabra a adivinar es de {len(guiones)} letras: ", " ".join(guiones))
print("\n")

while vidas > 0:
    letra = pedir_letra()
    letra_valida = validar_letra(letra)

    if (letra_valida):
        # Lógica que corre cuando la letra es correcta
        letra_en_palabra = esta_letra_en_palabra(letra_valida, palabra_seleccionada)
        if letra_en_palabra:
            guiones = mostrar_guiones_correctos(letra_valida, palabra_seleccionada, guiones)
            print("\n")
            print(f"Ha encontrado una letra en la palabra secreta: {" ".join(guiones)}")

            if (completo_palabra(guiones)):
                print("Fin del juego: ganaste")
                print("La palabra secreta es: ", "".join(guiones))
                break
            else:
                print("El juego sigue... \n")  # termina el juego

        # Lógica que corre cuando la letra NO es correcta
        else:
            print("\n")
            letras_incorrectas.append(letra_valida)
            print(f"La letra {letra_valida} no esta en la palabra secreta.")
            print(f"Letras incorrectas ingresadas: {",".join(letras_incorrectas)}")
            vidas = vidas - 1
            print(f"Oportunidades faltantes {vidas}")

            if vidas >= 1:
                print("\nEl juego sigue... ", " ".join(guiones), "\n")
                pass
            else:
                print("\nFin del juego: perdiste. AHORCADO :(", " La palabra era: {}".format(palabra_seleccionada))
                break