# Reconocimiento Facial para Control de Ingresos

Este programa utiliza reconocimiento facial para identificar empleados y registrar sus ingresos automáticamente. Funciona de la siguiente manera:

- *Cargar Imágenes:* Carga las imágenes de los empleados desde una carpeta específica y guarda sus nombres.
- *Codificar Imágenes:* Convierte las imágenes cargadas en un formato que permite comparar y reconocer caras.
- *Captura de Cámara:* Toma una imagen en tiempo real usando la cámara web.
- *Reconocimiento Facial:* Compara la cara capturada con las imágenes de los empleados previamente codificadas para identificar coincidencias.
- *Registro de Ingresos:* Si se encuentra una coincidencia, registra el nombre del empleado y la hora de ingreso en un archivo CSV.
- *Visualización:* Muestra la imagen capturada con un recuadro alrededor de la cara reconocida y el nombre del empleado en pantalla.


## Para ejecutar el programa

Busca el archivo setup_and_run.sh y ejecuta el siguiente comando en consola:

```sh
chmod +x setup_and_run.sh
```

luego escribe en consola:

```sh
./setup_and_run.sh
```