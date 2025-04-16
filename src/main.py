import os
from matrices import generar_matriz, determinante_gauss, inversa
from pylatex import Document, Section, Math, NewLine
from pylatex.utils import NoEscape
from flujos import obtener_flujo 

# Función para crear directorios si no existen
def crear_directorios():
    # Crear las carpetas de salida si no existen
    if not os.path.exists('output/pdf'):
        os.makedirs('output/pdf')
    if not os.path.exists('output/tex'):
        os.makedirs('output/tex')

# Función para obtener la entrada del usuario
def obtener_entrada_usuario():
    # Mostrar el menú con las opciones de tipo de matriz
    print("Selecciona el tipo de matriz ingresando el número correspondiente:")
    print("1. Cuadrada")
    print("2. Rectangular")
    print("3. Diagonal")
    print("4. Triangular Superior")
    print("5. Triangular Inferior")
    print("6. Identidad")
    print("7. Nula")
    print("8. Fila")
    print("9. Columna")

    # Solicitar al usuario el número correspondiente
    try:
        opcion = int(input("Ingresa el número correspondiente a tu tipo de matriz: "))
    except ValueError:
        print("Error: Debes ingresar un número válido.")
        return None, None, None, None

    # Validación de la opción seleccionada
    if opcion not in range(1, 10):
        print("Error: Opción no válida. Por favor selecciona un número del 1 al 9.")
        return None, None, None, None

    # Mapeo de opciones
    tipo_matriz = {
        1: "cuadrada",
        2: "rectangular",
        3: "diagonal",
        4: "triangular_superior",
        5: "triangular_inferior",
        6: "identidad",
        7: "nula",
        8: "fila",
        9: "columna"
    }[opcion]

    # Mensaje de recomendación basado en la opción seleccionada
    if tipo_matriz == "cuadrada":
        print("Una matriz cuadrada tiene el mismo número de filas y columnas. Ejemplo: 3x3, 4x4.")
        print("SE RECOMIENDA QUE INGRESES VALORES DE FILAS Y COLUMNAS DE 2x2 A 10x10.")
        mensaje_determinante = "SE CALCULARÁ EL DETERMINANTE PARA ESTA MATRIZ."
    elif tipo_matriz == "rectangular":
        print("Una matriz rectangular tiene un número diferente de filas y columnas. Ejemplo: 3*2, 4*5.")
        print("SE RECOMIENDA QUE INGRESES VALORES DE FILAS Y COLUMNAS ENTRE 2x3 Y 10x5.")
        mensaje_determinante = "SE CALCULARÁ EL DETERMINANTE PARA ESTA MATRIZ."
    else:
        mensaje_determinante = "SE CALCULARÁ EL DETERMINANTE O MATRIZ INVERSA SEGÚN CORRESPONDA."

    # Solicitar al usuario el tamaño de la matriz en formato filas*columnas (por ejemplo, 3*2)
    tamaño = input("Ingresa el tamaño de la matriz en formato filas*columnas (por ejemplo, 3*2): ").strip()

    try:
        filas, columnas = map(int, tamaño.split('*'))  # Convertir la entrada en enteros
    except ValueError:
        print("Error: El formato ingresado no es válido. Usa el formato filas*columnas.")
        return None, None, None, mensaje_determinante

    return tipo_matriz, filas, columnas, mensaje_determinante

# Obtener entradas del usuario
tipo_matriz, filas, columnas, mensaje_determinante = obtener_entrada_usuario()

# Si el tipo de matriz es inválido o las condiciones no se cumplen, salir
if tipo_matriz is None:
    exit()

# Imprimir mensaje sobre el determinante
print(mensaje_determinante)

# Obtener el flujo de pasos para el cálculo desde flujos.py
pasos_calculo = obtener_flujo(tipo_matriz)

# Mostrar los pasos de cálculo (solo los primeros 2 pasos)
print("\nPasos del cálculo:")
for paso in pasos_calculo[:2]:
    print(paso)

# Generar la matriz con los valores proporcionados
from matrices import generar_matriz
matriz = generar_matriz(tipo_matriz, filas, columnas)

# Calcular el determinante de la matriz (si es cuadrada)
if filas == columnas:
    determinante = determinante_gauss(matriz)
else:
    determinante = None

# Calcular la inversa de la matriz (si es cuadrada)
if filas == columnas:
    inversa_matriz = inversa(matriz)
else:
    inversa_matriz = None

# Función para generar el documento LaTeX
from flujos import obtener_flujo  # Importamos la función desde flujos.py
from pylatex import Document, Section, Math, NewLine
from pylatex.utils import NoEscape

# Función para generar el documento LaTeX
def generar_documento_latex(matriz, determinante, inversa):
    doc = Document()
    doc.preamble.append(NoEscape(r'\usepackage{amsmath}'))  # Aseguramos que amsmath esté cargado
    doc.preamble.append(NoEscape(r'\usepackage{graphicx}'))  # Aseguramos que graphicx esté cargado

    with doc.create(Section('Matrices y Operaciones')):
        # Mostrar la matriz generada
        doc.append('Matriz generada:')
        doc.append(NewLine())  # Añadimos un salto de línea
        doc.append(Math(data=[NoEscape(r'\begin{bmatrix} %s \end{bmatrix}' % '\\\\'.join([' & '.join(map(str, fila)) for fila in matriz]) )]))
        doc.append(NewLine())  # Añadimos un salto de línea después de la matriz

        # Mostrar el determinante
        doc.append('Determinante:')
        if determinante is not None:
            doc.append(Math(data=[str(determinante)]))
        else:
            doc.append("No se puede calcular el determinante para matrices no cuadradas.")
        doc.append(NewLine())
        
        # Mostrar los pasos para el cálculo del determinante
        doc.append("Pasos para el cálculo del determinante:")
        doc.append(NewLine())  # Salto de línea entre título y paso 1
        doc.append("Paso 1: Aplicamos la eliminación de Gauss para triangular la matriz.")
        doc.append(NewLine())
        doc.append("En este paso, se transforman los elementos de la matriz en ceros debajo de la diagonal principal usando operaciones elementales sobre las filas.")
        doc.append(NewLine())  # Añadimos salto de línea entre los pasos
        doc.append("Paso 2: Calculamos el determinante como el producto de los elementos de la diagonal de la matriz triangular.")
        doc.append(NewLine()) 
        doc.append("Fórmula: $\\text{det}(A) = \\prod_{i=1}^{n} a_{ii}$")  # Aquí usamos LaTeX para la fórmula
        doc.append(NewLine())  # Añadimos salto de línea después de la fórmula
        doc.append(NewLine())

        # Mostrar la inversa
        doc.append('Matriz inversa:')
        doc.append(NewLine())  # Añadimos salto de línea entre el título y la matriz
        if inversa is not None:
            doc.append(NoEscape(r'\resizebox{\textwidth}{!}{$\displaystyle \begin{bmatrix} %s \end{bmatrix}$}' % '\\\\'.join([' & '.join(map(str, fila)) for fila in inversa])))
        else:
            doc.append('No existe (determinante igual a cero o no es cuadrada).')
        doc.append(NewLine())  # Añadimos un salto de línea después de la matriz inversa

        # Mostrar los pasos para calcular la inversa
        if inversa is not None:
            doc.append(NewLine())  # Añadimos salto de línea entre la matriz inversa y los pasos
            doc.append("Pasos para calcular la matriz inversa:")
            doc.append(NewLine())  # Añadimos salto de línea después del título de los pasos
            doc.append("Paso 1: Calcular la matriz de cofactores.")
            doc.append(NewLine())  # Añadimos salto de línea entre los pasos
            doc.append("La matriz de cofactores se calcula aplicando la fórmula del cofactor $C_{ij} = (-1)^{i+j} \\cdot \\text{det}(M_{ij})$, donde $M_{ij}$ es la submatriz resultante al eliminar la fila i y la columna j.")
            doc.append(NewLine())  # Añadimos salto de línea entre los pasos
            doc.append("Paso 2: Calcular la adjunta.")
            doc.append(NewLine())  # Añadimos salto de línea entre los pasos
            doc.append("La adjunta de una matriz es la transpuesta de la matriz de cofactores.")
            doc.append(NewLine())  # Añadimos salto de línea entre los pasos
            doc.append("Paso 3: Calcular la matriz inversa usando la fórmula:")
            doc.append(NewLine())  # Añadimos salto de línea entre los pasos
            doc.append("$A^{-1} = \\frac{1}{\\text{det}(A)} \\cdot \\text{adj}(A)$")  # Fórmula de la inversa en LaTeX
            doc.append(NewLine())  # Añadimos salto de línea después de la fórmula

    # Generar los archivos en las carpetas respectivas
    doc.generate_pdf('output/pdf/matrices_operaciones', clean_tex=False)  # Guardar en la carpeta pdf
    doc.generate_tex('output/tex/matrices_operaciones')  # Guardar en la carpeta tex

# Crear directorios antes de generar el documento
crear_directorios()

# Llamar a la función para generar el documento
generar_documento_latex(matriz, determinante, inversa_matriz)

# Mensajes finales
print("Cálculo finalizado.")
print("El archivo 'matrices_operaciones.pdf' contiene la respuesta a sus datos ingresados.")
