def obtener_flujo(tipo_matriz):
    flujo = {
        "cuadrada": [
            "Paso 1: Aplicamos la eliminación de Gauss para triangular la matriz.",
            "Paso 2: Calculamos el determinante como el producto de los elementos de la diagonal.",
            "Paso 3: Calcular la matriz de cofactores.",
            "Paso 4: Calcular la adjunta y la inversa de la matriz usando la fórmula A^-1 = 1/det(A) * adj(A)."
        ],
        "rectangular": [
            "El determinante no se puede calcular para matrices rectangulares."
        ],
        "diagonal": [
            "Paso 1: Verificamos que la matriz sea cuadrada.",
            "Paso 2: El determinante es el producto de los elementos de la diagonal."
        ],
        "triangular_superior": [
            "Paso 1: Verificamos que la matriz sea cuadrada.",
            "Paso 2: El determinante es el producto de los elementos de la diagonal."
        ],
        "triangular_inferior": [
            "Paso 1: Verificamos que la matriz sea cuadrada.",
            "Paso 2: El determinante es el producto de los elementos de la diagonal."
        ],
        "identidad": [
            "Paso 1: La matriz es cuadrada.",
            "Paso 2: El determinante de la matriz identidad siempre es 1."
        ],
        "nula": [
            "El determinante de una matriz nula es 0."
        ],
        "fila": [
            "El determinante no se puede calcular para matrices fila."
        ],
        "columna": [
            "El determinante no se puede calcular para matrices columna."
        ]
    }
    return flujo.get(tipo_matriz, [])
