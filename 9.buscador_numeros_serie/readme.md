# Buscador de números de serie

Este programa se encarga de encontrar en una serie de archivos de texto, unos códigos
que tienen el siguiente patron: Nryu-12365 por medio de una regex y finalmente generando un reporte.

La presentación en pantalla de los hallazgos debe ser un listado en formato de tabla, que respete el siguiente formato de ejemplo:

```
----------------------------------------------------
Fecha de búsqueda: [fecha de hoy]

ARCHIVO		NRO. SERIE
-------		----------
texto1.txt	Nter-15496
texto25.txt	Ngba-85235

Números encontrados: 2
Duración de la búsqueda: 1 segundos
----------------------------------------------------
```

## Para ejecutar el script programa

Entrar a la carpeta buscador_numeros_serie y en una consola:

```sh
python buscador_numeros_serie.py
```

