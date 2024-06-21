#!/bin/bash

# Paso 1: Crea entono virtual de Python
echo "Creando un entorno virtual de Python..."
python3 -m venv venv

# Paso 2: Activar el entorno virtual
echo "Activando el entorno virtual..."
source venv/bin/activate

# Paso 3: Informar al usuario que el entorno esta listo
echo "El entorno virtual está listo y activado"

# paso 4: Instalar Tkinter 8.6.9 según el sistema operativo
if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  echo "Instaladno tkinter en Linux..."
  sudo apt-get install python3-tk
elif [[ "$OSTYPE" == "darwin"* ]]; then
  echo "Instalando Tkinter en macOS..."
  brew install python-tk
elif [[ "$OSTYPE" == "msys" ]]; then
  echo "Tkinter ya está instalado en Windows."
else
  echo "Sistema operativo no compatible."
fi

# Paso 5: Ejecutar el programa de python
echo "Ejecutando el script de python"
python main.py


