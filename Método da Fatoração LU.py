""" Carlos Eduardo dos Santos Cavalheiro 118302
    Método: Fatoração LU
    Resumo: A fatoração LU é uma decomposição de uma matriz A em um produto de duas matrizes: uma matriz triangular inferior L e uma matriz triangular superior U
    """

import numpy as np

def fatoracao_LU(A):
    n = A.shape[0]  # Obtém o número de linhas/colunas da matriz A
    L = np.zeros((n, n))  # Crio a matriz L como uma matriz zerada de tamanho N x N
    U = np.zeros((n, n))  # Crio a matriz U como uma matriz zerada de tamanho N x N

    for i in range(n):  # Loop para fazer a matrizes U e L
        for k in range(i, n):  # loop para preencher a matriz triangular superior (U)
            sum = 0  # Crio a variável para a soma calcular o elemento U[i][k]
            for j in range(i):  # loop de j=0 a i-1 
                sum += (L[i][j] * U[j][k]) #Soma os produtos L[i][j] e U[j][k]
            U[i][k] = A[i][k] - sum  # Calcula o elemento U[i][k]

        for k in range(i, n):  # loop para preencher a matriz triangular inferior (L)
            if i == k:
                L[i][i] = 1  # Define a diagonal de L como 1
            else:
                sum = 0  # Crio a variável para a soma calcular o elemento L[k][i]
                for j in range(i): # loop de j=0 a i-1 
                    sum += (L[k][j] * U[j][i]) # Soma os produtos L[k][j] e U[j][i]
                L[k][i] = (A[k][i] - sum) / U[i][i]  # Calcula o elemento L[k][i]

    return L, U  # Retorna as matrizes L e U

# Exemplo usado:
A = np.array([[3, -0.1, -0.2],
              [-0.1, 7, -0.3],
              [-0.3, -0.2, 10]], dtype=float)

L, U = fatoracao_LU(A)  # chamo a função

#prints para ver a resposta
print("Matrix Inicial:")
print(A)
print("\nMatriz triangular inferior (L):")
print(L)
print("\nMatriz triangular superior (U):")
print(U)
