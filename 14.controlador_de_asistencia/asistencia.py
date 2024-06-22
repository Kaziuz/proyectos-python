import cv2
import face_recognition as fr
import os
import numpy
from datetime import datetime

# Cargar las imagenes
ruta = 'Empleados'
mis_imagenes = []
nombres_empleados = []
lista_empleados = os.listdir(ruta)

for nombre in lista_empleados:
    imagen_actual = cv2.imread(f'{ruta}/{nombre}')
    if imagen_actual is None:
        print(f"Error al cargar la imagen: {ruta}/{nombre}")
        continue
    mis_imagenes.append(imagen_actual)
    nombres_empleados.append(os.path.splitext(nombre)[0])

# codificar imagenes
def codificar(imagenes):
    # crear una lista nueva
    lista_codificada = []

    # pasar todas las imagenes a rgb
    for imagen in imagenes:
        imagen = cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB)
        # buscamos caras
        caras_codificadas = fr.face_encodings(imagen)
        if not caras_codificadas:
            print("No se encontraron caras en la imagen")
            continue
        # agregamos a la lista
        lista_codificada.append(caras_codificadas[0])

    # devolver la lista codificada
    return lista_codificada

# registrar los ingresos
def registrar_ingresos(persona):
    with open("registro.csv", "a+") as registro:
        lista_datos = registro.readlines()
        nombres_registro = []
        for linea in lista_datos:
            ingreso = linea.split(',')
            nombres_registro.append(ingreso[0])

        if persona not in nombres_registro:
            ahora = datetime.now()
            string_ahora = ahora.strftime('%H:%M:%S')
            registro.writelines(f"\n{persona}, {string_ahora}")


lista_empleados_codificada = codificar(mis_imagenes)

# tomar una imagen de cámara web
# captura = cv2.VideoCapture(0, cv2.CAP_DSHOW) windows
captura = cv2.VideoCapture(0, cv2.CAP_ANY)

# leer imagen de la cámara
exito, imagen = captura.read()

if not exito:
    print("No se ha podido tomar la captura", exito)
else:
    # reconocer cara en la captura
    cara_captura = fr.face_locations(imagen)
    # codificar cara capturada
    cara_captura_codificada = fr.face_encodings(imagen, cara_captura)
    # buscar coincidencias
    for caracodif, caraubic in zip(cara_captura_codificada, cara_captura):
        coincidencias = fr.compare_faces(lista_empleados_codificada, caracodif)
        distancias = fr.face_distance(lista_empleados_codificada, caracodif)
        indice_coincidencia = numpy.argmin(distancias)
        # mostrar coincidencias si las hay
        if distancias[indice_coincidencia] > 0.6:
            print("No coincide con ninguna persona")
        else:
            print("bienvenido")
            # buscar el nombre del empleado encontrado
            nombre = nombres_empleados[indice_coincidencia]

            # dibujar cuadrado sobre la imagen
            y1, x2, y2, x1 = caraubic
            cv2.rectangle(imagen, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(imagen, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(imagen, nombre, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            registrar_ingresos(nombre)
            # mostrar imagen obtenida
            cv2.imshow('Imagen web', imagen)
            # mantener ventana abierta
            cv2.waitKey(0)

