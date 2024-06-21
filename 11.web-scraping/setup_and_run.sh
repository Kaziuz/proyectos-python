#!/bin/bash

# Paso 1: Crea entono virtual de Python
echo "Creando un entorno virtual de Python..."
python3 -m venv venv

# Paso 2: Activar el entorno virtual
echo "Activando el entorno virtual..."
source venv/bin/activate

# Paso 3: Instalar las librerias del archivo requirements.txt
echo "Instalando las librerias..."
pip install -r requirements.txt

# Paso 4: Informar al usuario que el entorno esta listo
echo "El entorno virtual está listo y las librerias se han instalado"

# Paso 5: Ejecutar el programa de python
echo "Ejecutando el script de python"
python scraping-book-store.py


