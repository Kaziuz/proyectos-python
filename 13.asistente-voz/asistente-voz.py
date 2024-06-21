# Asistente de voz

""" Voces
monica = "Mónica"
montse = "Montse"
paulina = "Paulina"
"""

from gtts import gTTS
import os
import speech_recognition as sr
from io import BytesIO
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


# Escuchar nuestro micrófono y devolver el audio como texto
def transformar_audio_en_texto():
    # Almacenar recognizer en variable
    r = sr.Recognizer()

    # Configurar el micrófono
    with sr.Microphone() as origen:

        # Tiempo de espera
        r.pause_threshold = 0.8

        # Informar que comenzó la grabación
        print("Ya puedes hablar")

        # Guardar lo que se escucho en micrófono
        audio = r.listen(origen)

        try:
            # Buscar en google lo que haya escuchado
            pedido = r.recognize_google(audio, language="es-US")

            # Prueba de que pudo ingresar
            print("Dijiste: " + pedido)

            # Devolver el pedido
            return pedido

        except sr.UnknownValueError:
            # No comprendió el audio
            print("upppssss, no entendí")
            # Devolver error
            return "Sigo esperando"

        except sr.RequestError:
            # No resolvió el pedido
            print("upppssss, no hay servicio")
            # Devolver error
            return "Sigo esperando"

        except Exception as e:
            # Error inesperado
            print(f"upppssss, algo ha salido mal {e}")
            # Devolver error
            return "Sigo esperando"


# El asistente habla usando google
def hablar_google(mensaje):
    try:
        tts = gTTS(text=mensaje, lang='es', tld='us')
        tts.save("mensaje.mp3")  # guardamos el mensaje como mp3
        os.system("afplay mensaje.mp3")  # La maquina dice el mensaje
        os.remove("mensaje.mp3")
    except Exception as e:
        print(f"No pude decir el mensaje: {e}")


# El asistente habla usando las voces del computador
def hablar_mac(mensaje, voz='Mónica'):
    try:
        os.system(f"say -v {voz} {mensaje}")
    except Exception as e:
        print(f"No pude decir el mensaje: {e}")


# Informar el dia de la semana
def pedir_dia():
    # Crear la variable con los datos de hoy
    dia = datetime.date.today()
    print(dia)
    # crear variable para el dia de la semana
    dia_semana = dia.weekday()
    print(dia_semana)
    dias = {
        0: "Lunes",
        1: "Martes",
        2: "Miércoles",
        3: "Jueves",
        4: "Viernes",
        5: "Sábado",
        6: "Domingo"
    }
    return dias[dia_semana]


# Informar la hora actual
def pedir_hora():
    tiempo = datetime.datetime.now()
    formato_am_pm = tiempo.strftime("%I:%M %p")
    # Dividimos el string en partes usando split
    partes = formato_am_pm.split(" ")  # ['HH:MM', 'AM/PM']
    hora_minutos = partes[0].split(":")  # ['HH', 'MM']
    am_pm = partes[1]  # 'AM' o 'PM'
    hora = int(hora_minutos[0])  # Convertimos la hora a entero
    minutos = int(hora_minutos[1])  # Convertimos los minutos a entero
    if am_pm == "AM":
        return f"Son las {hora} y {minutos} de la mañana"
    else:
        return f"Son las {hora} y {minutos} de la tarde"


def saludo_inicial(nombre="Alison"):
    tiempo = datetime.datetime.now()
    print(tiempo)
    if tiempo.hour <= 12:
        hablar_google(f"Buenos días. Cómo estás ?. Soy {nombre}, tu asistente personal. Por favor dime en que te "
                   f"puedo ayudar...")
    elif tiempo.hour >= 12 or tiempo.hour < 18:
        hablar_google(f"Buenas Tardes. Cómo estás ?. Soy {nombre}, tu asistente personal. Por favor dime en que te "
                   f"puedo ayudar...")
    else:
        hablar_google(f"Buenas Noches. Cómo estás ?. Soy {nombre}, tu asistente personal. Por favor dime en que te "
                   f"puedo ayudar...")


# Función central del asistente
def pedir_cosas():
    # activar el salido inicial
    saludo_inicial()

    # variable para terminar el asistente
    comenzar = True

    # loop central
    while comenzar:
        # activar el micrófono y guardar el pedido en un string
        pedido = transformar_audio_en_texto().lower()

        if 'youtube' in pedido:
            hablar_google('Con gusto, estoy abriendo youTube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'navegador' in pedido:
            hablar_google('Con gusto, estoy abriendo el navegador')
            webbrowser.open('https://www.google.com')
            continue
        elif 'día es hoy' in pedido:
            dia = pedir_dia()
            hablar_google(f"Hoy es {dia}")
            continue
        elif 'hora es' in pedido:
            hora = pedir_hora()
            hablar_google(hora)
            continue
        elif 'en wikipedia' in pedido:
            hablar_google('Buscando eso en wikipedia')
            pedido = pedido.replace('busca en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences=1)
            hablar_google('Wikipedia dice lo siguiente:')
            hablar_google(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar_google('Ya mismo estoy en eso...')
            pedido = pedido.replace("busca en internet", '')
            pywhatkit.search(pedido)
            hablar_google('Esto es lo que he encontrado: ')
            continue
        elif 'reproducir' in pedido:
            hablar_google('Buena idea, ya comienzo a reproducirlo')
            pywhatkit.playonyt(pedido)
            continue
        elif 'piroba' in pedido:
            hablar_google('mas pirobo seras voz gonorrea')
            continue
        elif 'chiste' in pedido:
            hablar_google('Ya te cuento un chiste')
            hablar_google(pyjokes.get_joke('es'))
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip() # encuentra la palabra final de la lista
            cartera = {'Apple': 'APPL', 'amazon': 'AMZN', 'google': 'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar_google(f"La encontré, el precio de {accion} es {precio_actual}")
                continue
            except:
                hablar_google("Perdón, pero no la he encontrado")
                continue
        elif 'adiós' in pedido:
            hablar_google('Ya me voy a descansar, cualquier cosa me avisas')
            break

pedir_cosas()
