import numpy as np
from random import randint

def generar_matriz(tipo, filas, columnas):
    if tipo == 'cuadrada':
        return np.random.randint(1, 10, size=(filas, filas))
    elif tipo == 'rectangular':
        return np.random.randint(1, 10, size=(filas, columnas))
    elif tipo == 'diagonal':
        diag = np.random.randint(1, 10, size=filas)
        return np.diag(diag)
    elif tipo == 'triangular_superior':
        return np.triu(np.random.randint(1, 10, size=(filas, columnas)))
    elif tipo == 'triangular_inferior':
        return np.tril(np.random.randint(1, 10, size=(filas, columnas)))
    elif tipo == 'identidad':
        return np.eye(filas)
    elif tipo == 'nula':
        return np.zeros((filas, columnas))
    elif tipo == 'fila':
        return np.random.randint(1, 10, size=(1, columnas))
    elif tipo == 'columna':
        return np.random.randint(1, 10, size=(filas, 1))
    else:
        raise ValueError("Tipo de matriz no reconocido.")

# Cálculo del determinante usando Gauss
def determinante_gauss(matriz):
    A = matriz.astype(float)
    n = len(A)
    for i in range(n):
        if A[i][i] == 0.0:
            return 0
        for j in range(i+1, n):
            ratio = A[j][i] / A[i][i]
            for k in range(i, n):
                A[j][k] -= ratio * A[i][k]
    det = 1
    for i in range(n):
        det *= A[i][i]
    return det

# Cálculo de la inversa usando cofactores
def inversa(matriz):
    n = len(matriz)
    A = matriz.astype(float)
    adj = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            cofactor = calcular_cofactor(A, i, j)
            adj[j][i] = ((-1) ** (i + j)) * cofactor
    det = determinante_gauss(A)
    if det == 0:
        return None  # La matriz no tiene inversa
    return adj / det

# Cálculo del cofactor
def calcular_cofactor(matriz, fila, columna):
    submatriz = np.delete(matriz, fila, axis=0)
    submatriz = np.delete(submatriz, columna, axis=1)
    return determinante_gauss(submatriz)
