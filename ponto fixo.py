from math import e #importando a constante euler
""" Carlos Eduardo dos Santos Cavalheiro 118302
    f(x) = (e**-x)-x
    0 = (e**-x)-x
    x =  e**-x"""
def ponto_fixo(): #definindo a função
    Xi = 0 #criando a variável do chute inicial
    tolerancia = 0.05 #criando a variável da tolerancia
    for n in range(0, 100, 1): #criando o limite de iterações
        X = e**-Xi #calculo do valor de X
        erro = abs((X-Xi)/X) #calculo do valor do erro
        print(f"iteração= {n}, Xi= {Xi}, erro = {erro}") #prints para acompanhar os resultados
        if(erro<=tolerancia): #teste para parar quando atingir a tolerancia
            return erro #retorno do valor de erro para encerrar a função
        else: #caso o erro seja maior que a tolerancia
            Xi = X #atualização do valor de Xi
            X=erro #atualização do valor de X

ponto_fixo()