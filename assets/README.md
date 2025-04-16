# Proyecto de Cálculo de Matrices

Este proyecto permite generar matrices aleatorias de diferentes tipos, calcular determinantes utilizando el método de Gauss, calcular la matriz inversa y generar un documento LaTeX que muestra los resultados. El programa está escrito en **Python** y utiliza **PyLaTeX** para generar el documento LaTeX y renderizar las fórmulas matemáticas.

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

AlgebraLineal/
│
├── src/
│   ├── main.py          # Código principal que genera la matriz, calculando la inversa y determinante
│   ├── matrices.py      # Funciones que generan las matrices y calculan el determinante y la inversa
│   ├── flujos.py        # Funciones que gestionan los flujos de pasos para el cálculo
│   ├── output/          # Carpeta donde se guardan los archivos generados
│   │   ├── pdf/         # Archivos PDF generados
│   │   └── tex/         # Archivos LaTeX generados
│
└── README.md            # Este archivo
