"""
# Proyecto de Cálculo de Matrices

Este proyecto en Python permite generar matrices aleatorias de diferentes tipos, calcular determinantes utilizando el método de Gauss, calcular la matriz inversa y generar un documento LaTeX que muestra los resultados. El programa está escrito en **Python** y utiliza **PyLaTeX** para generar el documento LaTeX y renderizar las fórmulas matemáticas.

## Información del grupo

- **Javier David Jiménez Plata**  
  Código: **2150009**

- **Natalia Estefanía Daza Medina**  
  Código: **2150010**

## Requisitos

Antes de ejecutar el programa, asegúrate de tener instalado lo siguiente:

1. **Python 3.x**  
   El proyecto fue desarrollado y probado con Python 3.11, pero debería funcionar con cualquier versión reciente de Python 3.

2. **Librerías de Python**  
   Asegúrate de tener instaladas las siguientes librerías:
   - `pylatex`: Para generar el documento LaTeX.
   - `numpy`: Para las operaciones con matrices.
   - `latexmk` o `pdflatex`: Necesarios para compilar el archivo LaTeX a PDF.

3. **MiKTeX (en Windows)** o **TeX Live (en Linux y macOS)**  
   Necesitarás una distribución de LaTeX para compilar los archivos generados. Aquí está la información sobre la instalación:

   ### **Instalar PyLaTeX y dependencias**:

   Abre tu terminal o consola de comandos y ejecuta lo siguiente para instalar las dependencias de Python:
   ```bash
   pip install pylatex numpy

   ### **Instalar LaTeX (MiKTeX o TeX Live)**:
   - En **Windows**, puedes descargar **MiKTeX** desde:  
     [https://miktex.org/download](https://miktex.org/download)
   
   - En **Linux (Ubuntu)**, puedes instalar **TeX Live** ejecutando:
     ```bash
     sudo apt-get install texlive-full
     ```

   - En **macOS**, puedes instalar **MacTeX** ejecutando:
     ```bash
     brew install --cask mactex
     ```

   Después de instalar MiKTeX o TeX Live, asegúrate de que la ruta a los ejecutables `pdflatex` o `latexmk` esté configurada correctamente en tu variable de entorno **PATH**.

## Instalación

### **Cómo descargar el proyecto**:
Para descargar el proyecto, puedes clonarlo desde GitHub utilizando **Git** o simplemente descargando el archivo ZIP.

1. **Clonar usando Git**:
   ```bash
   git clone https://github.com/javierjimenezdp/AlgebraLineal.git
### **Descargar como archivo ZIP**:
   Si prefieres no usar Git, puedes descargar el repositorio como un archivo ZIP directamente desde la página de GitHub:
   [https://github.com/javierjimenezdp/AlgebraLineal](https://github.com/javierjimenezdp/AlgebraLineal)  
   Haz clic en el botón **"Code"** y selecciona **"Download ZIP"**.

### **Instalar dependencias**:
   Después de haber descargado el proyecto, navega hasta la carpeta donde se encuentra el código y ejecuta:
   ```bash
   cd AlgebraLineal
   pip install -r requirements.txt
### **¿Cómo ejecutar el programa?**

1. **Ejecuta el archivo principal**:
   Para ejecutar el programa, abre la terminal o consola de comandos y navega a la carpeta donde descargaste el proyecto. Luego ejecuta el siguiente comando:
   ```bash
   python src/main.py
"""

