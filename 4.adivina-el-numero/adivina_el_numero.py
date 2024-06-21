# Adivina el numero

from random import randint

name_user = input("Escriba su nombre: ")

generated_number = randint(1, 100)

print(f"\nBueno {name_user}, he pensado un numero entre 1 y 100.\nTienes solo 8 intentos para adivinar el número.\n")

attempts = 8
attempts_counter = 1
number_user = 0

while attempts_counter <= attempts:
    number_user = int(input(f"Ingrese un número. Es el intento {attempts_counter}: "))
    attempts_counter += 1

    if (number_user < 0) or (number_user > 101):
        print(F"El número {number_user} no esta permitido. Deben de ser números entre 1 y 100 \n")

    elif number_user < generated_number:
        print(f"El número {number_user} es menor al número secreto \n")

    elif number_user > generated_number:
        print(f"El número {number_user} es mayor al número secreto \n")

    elif number_user == generated_number:
        print(f"Ganaste, El número {number_user} es el número que he pensado.")
        print(f"Necesitaste {attempts_counter-1} intentos para adivinar el número. \n")
        break

if number_user != generated_number:
    print("\n")
    print(f"No pudiste adivinar el número :(, el número era: {generated_number}")
