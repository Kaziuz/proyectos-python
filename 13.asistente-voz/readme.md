# Asistente de voz

Este programa es un asistente de voz que puede realizar diversas tareas a partir de comandos hablados del usuario. Sus funcionalidades principales son:

- *Reconocimiento de Voz:* Escucha y convierte el audio del usuario en texto utilizando la librería speech_recognition.
- *Conversión de Texto a Voz:* Responde al usuario hablando mediante la librería gTTS o usando las voces integradas del sistema operativo.
- *Interacción y Respuestas:*
	•	Saludo Inicial: Saluda al usuario según la hora del día.
	•	Abrir YouTube o el Navegador: Abre YouTube o un navegador web a petición del usuario.
	•	Información del Día y Hora: Informa sobre el día de la semana y la hora actual.
	•	Búsqueda en Wikipedia: Busca y resume información de Wikipedia.
	•	Búsqueda en Internet: Realiza búsquedas en Internet.
	•	Reproducción de Videos en YouTube: Reproduce videos en YouTube.
	•	Contar Chistes: Cuenta chistes.
	•	Precio de Acciones: Informa sobre el precio actual de ciertas acciones.
	•	Despedida: Termina la sesión cuando el usuario dice “adiós”.

## Uso

El asistente está diseñado para interactuar de forma continua con el usuario, respondiendo a sus comandos y proporcionando información útil. Se puede utilizar para tareas comunes como buscar información, reproducir música o videos, y obtener actualizaciones de tiempo y fecha.

## Para ejecutar el asistente

Busca el archivo setup_and_run.sh y ejecuta el siguiente comando en consola:

```sh
chmod +x setup_and_run.sh
```

luego escribe en consola:

```sh
./setup_and_run.sh
```