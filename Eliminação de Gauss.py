""" Carlos Eduardo dos Santos Cavalheiro 118302
    Método: Eliminação de Gauss
    Resumo: A eliminação gaussiana, também conhecida como escalonamento, é um método direto para resolver sistemas lineares.
    Consiste em um algoritmo para eliminar variáveis (formando
um sistema triangular superior) e substituir regressivamente. Nesse caso o algoritmo que esta sendo executado é a matriz:
    2x1 + 100 000x2 = 100 000
    x1 + x2 = 2
    """

def gauss(A, b):
    n = len(A)  # Obtém o número de linhas da matriz A
    
    # Etapa de eliminação
    for i in range(n):
        # Pivoteamento parcial: encontra a linha com o maior valor absoluto na coluna i
        linha_m = i  # Atribui a linha_m o índice da linha
        for k in range(i + 1, n):
            if abs(A[k][i]) > abs(A[linha_m][i]):
                linha_m = k  # Atualiza linha_m com o maior valor absoluto na coluna i

        # Troca a linha atual com a linha linha_m
        A[i], A[linha_m] = A[linha_m], A[i]  # Troca as linhas na matriz A
        b[i], b[linha_m] = b[linha_m], b[i]  # Troca os elementos correspondentes no vetor b
        
        # Escalonamento: elimina os elementos abaixo do pivô
        for j in range(i + 1, n):
            fator = A[j][i] / A[i][i]  # Calcula o fator multiplicativo para zerar A[j][i]
            for k in range(i, n):
                A[j][k] -= fator * A[i][k]  # Atualiza a linha j subtraindo fator vezes a linha i
            b[j] -= fator * b[i]  # Atualiza o vetor b subtraindo fator vezes b[i]
    
    # Etapa de substituição de volta
    x = [0] * n  # Inicializa o vetor solução com zeros
    for i in range(n - 1, -1, -1):
        x[i] = b[i]  # Inicializa x[i] com b[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]  # Subtrai os termos conhecidos do lado direito
        x[i] /= A[i][i]  # Divide pelo coeficiente do pivô para obter o valor de x[i]
    
    return x  # Retorna o vetor solução

# Exemplo:
coeficientes = [[2, 100000],  # Matriz dos coeficientes
                [1, 1]]
TI =           [100000, 2]  # Matriz dos termos independentes

solution = gauss(coeficientes, TI)  # Chama a função gauss para resolver o sistema
print("Solução do sistema =", solution)  # Imprime a solução do sistema
