from math import e # importando o valor da constante euler
""" Carlos Eduardo dos Santos Cavalheiro 118302
    Método da secante
    resumo: O método da Secante é uma alternativa para o Método de Newton-Raphson, onde o cálculo da derivada pode ser um problema para implementar. Nesse se faz uso de
uma reta secante como uma aproximação da reta tangente em
um determinado ponto. Nesse método precisamos de duas estimativas iniciais, porém não precisamos de uma expressão analítica para a derivada. Porém, não é
exigido que a função mude de sinal entre as estimativas, por isso
não é um método intervalar.
    """
def metodo_Secante(f, x0, x1, tolerancia, limite): # definição da função do metodo da secante
    contador = 0 # definição do contador para parar caso atinja o limite de iterações

    while (contador < limite): # função para repetir os calculos ate encontrar a raiz aproximada ou atinjir o máximo de iterações
        
        f_x0 = f(x0) # calculo da função com o valor de x = x0
        f_x1 = f(x1) # calculo da função com o valor de x = x1

        x2 = x1 - (f_x1 * (x1 - x0) / (f_x1 - f_x0)) # calculo da raiz aproximada pelo metodo da sencate

        erro = abs(((x2-x1)/x2)) # calculo do erro percentual

        print(f"iteração = {contador} x0 = {x0}, x1 = {x1}, x2 = {x2}, erro = {erro}") # print para acompanhar os resultados em cada iteração

        if (erro < tolerancia): # teste para saber se deve parar ao atingir a tolerância
            print("Aproximação da raiz = ", x2) # print da raiz obtida
            return None

        x0 = x1 # atualização do valor de x0
        x1 = x2 # atualização do valor de x1
        contador += 1 # atualização do valor do contador

    print("Máximo de iterações atingido, Não foi possível encontrar a raiz") # resposta caso o limite de irações seja atingido
    return None

def f(x):
    return (e**-x)-x # definição da função

x0= 1 # definição do valor inicial de x0
x1 = 0 # definição do valor inicial de x1
tolerancia = 0.01 # definição do valor da tolerância
limite = 100 # definição do valor limite de iterações

metodo_Secante(f, x0, x1, tolerancia, limite) # execução da função