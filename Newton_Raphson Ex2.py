from math import e #importando euler
""" Carlos Eduardo dos Santos Cavalheiro 118302
    Método: Newton-Raphson
    resumo: O método de Newton-Raphson pode ser deduzido com base em sua
    interpretação geométrica. A inclinação da reta traçada é equivalente à f′(x), então: 
    tan ϕ = CO/CA
    f′(x) = (f (xi) − 0)/(xi − xi+1)
    que pode ser organizada da seguinte forma para obter a estimativa melhorada da raiz:
    xi+1 = xi −(f(xi)/f′(xi))
    que é a fórmula de Newton-Raphson
    """

def  Newton_Raphson(): #definindo a função
    Xi = 0.5 #criando a variável do chute inicial
    tolerancia = 1 #criando a variável da tolerancia
    for n in range(0, 100, 1): #criando o limite de iterações
        X = Xi-(((Xi**10)-1)/(10*(Xi**9))) #calculo do valor de X
        erro = abs(((X-Xi)/X)*100) #calculo do valor do erro
        print(f"iteração= {n}, Xi= {X}, erro = {erro}%") #prints para acompanhar os resultados
        if(erro<=tolerancia): #teste para parar quando atingir a tolerancia
            return erro #retorno do valor de erro para encerrar a função
        else: #caso o erro seja maior que a tolerancia
            Xi = X #atualização do valor de Xi
    print("não foi encontrada uma raiz dentro dos critérios definidos")#print caso nao encontre uma raiz
    
Newton_Raphson()